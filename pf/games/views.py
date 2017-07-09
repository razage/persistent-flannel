from flask import Blueprint, render_template

from .models import Game

mod = Blueprint("games", __name__, url_prefix="/games")


@mod.route('/<game_id>')
def view_game(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template("games/game_view.html", game=game)
