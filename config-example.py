from os.path import abspath, dirname, join

BASE_DIR = abspath(dirname(__file__))
NODE_DIR = join(BASE_DIR, "node_modules")

DEBUG = True
CSRF_SESSION_KEY = '***'
SECRET_KEY = '***'

SQLALCHEMY_DATABASE_URI = ('mysql://test:test123@localhost/pf?charset=utf8mb4')
