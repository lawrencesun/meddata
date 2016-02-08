from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, ValidationError
from wtforms.validators import Required, Email, Length, Regexp, NumberRange
from models import User

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    remember_me = BooleanField('Keep me logged in', default = False)

class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, numbers, dots or underscores')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')

class DataForm(Form):
	systolic_pressure = IntegerField('Systolic',validators=[Required(), NumberRange(min=20, max=200)])
	diastolic_pressure = IntegerField('Diastolic', validators=[Required(), NumberRange(min=20, max=200)])
	cardiac_rate = IntegerField('Cardiac', validators=[Required(), NumberRange(min=20, max=200)])