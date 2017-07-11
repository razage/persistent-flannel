import logging
from os.path import join

from flask import Flask
from flask_assets import Bundle, Environment
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'

db = SQLAlchemy(app)

ma = Marshmallow(app)

boot = Bootstrap(app)

assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle("scss/main.scss", filters='pyscss', output="css/main.css")

js_libs = [join(app.config['NODE_DIR'], 'jquery', 'dist', 'jquery.js'),
           join(app.config['NODE_DIR'], 'vue', 'dist', 'vue.js'),
           join(app.config['NODE_DIR'], 'bootstrap', 'dist', 'js', 'bootstrap.js')]

js_deps = Bundle(js_libs, filters='jsmin', output="js/deps.js")

assets.register('css_all', scss)
assets.register('js_libs', js_deps)

if app.config['DEBUG']:
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    toolbar = DebugToolbarExtension(app)
    app.logger.setLevel(logging.DEBUG)


    @app.after_request
    def forbid_cache(request):
        request.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
        request.headers['Pragma'] = 'no-cache'
        request.headers['Expires'] = '0'
        return request

else:
    app.logger.setLevel(logging.WARNING)

from .views import *
