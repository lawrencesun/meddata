
from flask import Flask, g, request
#from flask_sqlalchemy import SQLAlchemy
# lower version:
from flask.ext.sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.debug = True
app.config.from_object('config')
db = SQLAlchemy(app)


from views import *

if __name__ == '__main__':
    app.run()
