from flask import abort, render_template

from . import app


@app.route("/")
def home():
    return render_template("base.html", title="Home")

# Blueprint registration
from .games.views import mod as games_mod

app.register_blueprint(games_mod)
