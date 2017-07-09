from flask import render_template

from . import app
from .games.views import mod as games_mod
from .users.views import mod as user_mod


@app.route("/")
def home():
    return render_template("base.html", title="Home")

# Blueprint registration
app.register_blueprint(games_mod)
app.register_blueprint(user_mod)
