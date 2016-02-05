from myapp import db

# User
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    datas = db.relationship('Data', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

# Data
class Data(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	systolic_pressure = db.Column(db.Integer, default = 0)
	diastolic_pressure = db.Column(db.Integer, default = 0)
	cardiac_rate = db.Column(db.Integer, default = 0)
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
        return '<Data %r>' % self.cardiac_rate