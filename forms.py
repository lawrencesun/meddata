from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import Required, Email, Length

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    remember_me = BooleanField('Keep me logged in', default = False)