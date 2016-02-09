import os
import sys

root = os.path.dirname(__file__)

# sys.path.insert(0, os.path.join(root, 'site-packages'))
sys.path.insert(0, os.path.join(root, 'site-packages.zip'))

import sae
from myapp import app, db
db.create_all()
application = sae.create_wsgi_app(app)