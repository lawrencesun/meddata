
from flask import Flask, g, request
#from flask_sqlalchemy import SQLAlchemy
# lower version:
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.login import LoginManager

app = Flask(__name__)
app.debug = True
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

from views import *

if __name__ == '__main__':
    app.run()
