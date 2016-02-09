from flask import Flask, render_template, url_for, redirect, request, flash, session, g, abort
from flask.ext.login import login_user, logout_user, current_user, login_required
from myapp import app, db, lm
from forms import LoginForm, RegistrationForm, DataForm
from models import User, Data
import datetime
from sqlalchemy import func
from config import DATAS_PER_PAGE

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/index/<int:page>', methods = ['GET', 'POST'])
@login_required
def index(page = 1):
	form = DataForm()
	user_data = Data.query.filter_by(user_id = g.user.id)
	#ms = user_data.order_by(Data.systolic_pressure.desc()).first()
	four_weeks_ago = datetime.datetime.now() - datetime.timedelta(weeks=4)

	maxs = db.session.query(func.max(Data.systolic_pressure).label('max_systolic')).filter_by(user_id = g.user.id).one()
	max_systolic = maxs.max_systolic
	mins = db.session.query(func.min(Data.systolic_pressure).label('min_systolic')).filter_by(user_id = g.user.id).one()
	min_systolic = mins.min_systolic
	avgs = db.session.query(func.avg(Data.systolic_pressure).label('avg_systolic')).filter_by(user_id = g.user.id).\
			filter(Data.timestamp > four_weeks_ago).one()
	avg_systolic = avgs.avg_systolic

	maxd = db.session.query(func.max(Data.diastolic_pressure).label('max_diastolic')).filter_by(user_id = g.user.id).one()
	max_diastolic = maxd.max_diastolic
	mind = db.session.query(func.min(Data.diastolic_pressure).label('min_diastolic')).filter_by(user_id = g.user.id).one()
	min_diastolic = mind.min_diastolic
	avgd = db.session.query(func.avg(Data.diastolic_pressure).label('avg_diastolic')).filter_by(user_id = g.user.id).\
			filter(Data.timestamp > four_weeks_ago).one()
	avg_diastolic = avgd.avg_diastolic

	maxc = db.session.query(func.max(Data.cardiac_rate).label('max_rate')).filter_by(user_id = g.user.id).one()
	max_rate = maxc.max_rate
	minc = db.session.query(func.min(Data.cardiac_rate).label('min_rate')).filter_by(user_id = g.user.id).one()
	min_rate = minc.min_rate
	avgc = db.session.query(func.avg(Data.cardiac_rate).label('avg_rate')).filter_by(user_id = g.user.id).\
			filter(Data.timestamp > four_weeks_ago).one()
	avg_rate = avgc.avg_rate

	if form.validate_on_submit():
		data = Data(systolic_pressure = form.systolic_pressure.data,
					diastolic_pressure = form.diastolic_pressure.data,
					cardiac_rate = form.cardiac_rate.data,
					timestamp = datetime.datetime.now(),
					body = form.note.data,
					user = g.user)
		db.session.add(data)
		db.session.commit()
		db.session.close()
		flash('Added successfully')
		return redirect(url_for('index'))

	datas = user_data.order_by(Data.timestamp.desc()).paginate(page, DATAS_PER_PAGE, False)

	return render_template('index.html',
		title = 'Home',
		form = form,
		max_systolic = max_systolic,
		min_systolic = min_systolic,
		avg_systolic = avg_systolic,
		max_diastolic = max_diastolic,
		min_diastolic = min_diastolic,
		avg_diastolic = avg_diastolic,
		max_rate = max_rate,
		min_rate = min_rate,
		avg_rate = avg_rate,
		datas = datas)

@app.route('/entry', methods = ['GET', 'POST'])
@login_required
def entry():
	form = DataForm()
	if form.validate_on_submit():
		data = Data(systolic_pressure = form.systolic_pressure.data,
					diastolic_pressure = form.diastolic_pressure.data,
					cardiac_rate = form.cardiac_rate.data,
					timestamp = datetime.datetime.now(),
					body = form.note.data,
					user = g.user)
		db.session.add(data)
		db.session.commit()
		db.session.close()
		flash('Added successfully')
		return redirect(url_for('index'))
	return render_template('entry.html',
		title = 'Entry',
		form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None: 
			login_user(user, form.remember_me.data)
			return redirect(url_for('index'))
		flash('Invalid email address')
	return render_template('login.html',
		title = 'Sign In',
		form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username = form.username.data, 
					email = form.email.data)
		db.session.add(user)
		db.session.commit()
		db.session.close()
		flash("You can now login.")
		return redirect(url_for('login'))
	return render_template('register.html', 
		form = form)