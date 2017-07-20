from sqlalchemy_utils.types import CurrencyType, URLType

from pf import db
from pf.models import BaseModel

game_developer = db.Table("assoc_game_developers", db.Column("game_id", db.Integer, db.ForeignKey("games.id")),
                          db.Column("developer_id", db.Integer, db.ForeignKey("companies.id")))
game_publisher = db.Table("assoc_game_publishers", db.Column("game_id", db.Integer, db.ForeignKey("games.id")),
                          db.Column("publisher_id", db.Integer, db.ForeignKey("companies.id")))
game_genres = db.Table("assoc_game_genres", db.Column("game_id", db.Integer, db.ForeignKey("games.id")),
                       db.Column("genre_id", db.Integer, db.ForeignKey("tags.id")))
game_tags = db.Table("assoc_game_tags", db.Column("game_id", db.Integer, db.ForeignKey("games.id")),
                     db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")))


class Game(BaseModel):
    __tablename__ = "games"

    name = db.Column(db.String(32), unique=True, nullable=False)
    release_date = db.Column(db.Date)
    description = db.Column(db.Text)
    website = db.Column(URLType)

    developers = db.relationship('Company', secondary=game_developer, back_populates="developed_games")
    publishers = db.relationship('Company', secondary=game_publisher, back_populates="published_games")
    genres = db.relationship('Tag', secondary=game_genres, back_populates="games_in_genre")
    tags = db.relationship('Tag', secondary=game_tags, back_populates="games_in_tag")
    prices = db.relationship('GamePrice', back_populates="game")

    def __init__(self, name, release_date=None, description=None, website=None):
        self.name = name


class GamePrice(db.Model):
    __tablename__ = "game_prices"

    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), primary_key=True)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(CurrencyType, nullable=False)

    game = db.relationship('Game', back_populates="prices")

    def __init__(self, price, currency):
        self.price = price
        self.currency = currency
