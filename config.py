import os

CSRF_ENABLED = True
SECRET_KEY = 'you-can-guess'

# MySQL configuration
basedir = os.path.abspath(os.path.dirname(__file__))

MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'sun'
MYSQL_PASS = '123456'
MYSQL_DB = 'app'

SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' \
                          % (MYSQL_USER, MYSQL_PASS,
                             MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# pagination
DATAS_PER_PAGE = 3