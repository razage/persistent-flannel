from pf import db
from pf.models import BaseModel

game_developer = db.Table("assoc_game_developers", db.Column("game_id", db.Integer, db.ForeignKey("games.id")),
                          db.Column("developer_id", db.Integer, db.ForeignKey("companies.id")))
game_publisher = db.Table("assoc_game_publishers", db.Column("game_id", db.Integer, db.ForeignKey("games.id")),
                          db.Column("publisher_id", db.Integer, db.ForeignKey("companies.id")))


class Game(BaseModel):
    __tablename__ = "games"

    name = db.Column(db.String(32))
    release_date = db.Column(db.Date, nullable=True)

    developer = db.relationship("Company", secondary=game_developer)
    publisher = db.relationship("Company", secondary=game_publisher)
    info = db.relationship("GameInfo", uselist=False, back_populates="game")

    def __init__(self, name, release_date=None):
        self.name = name
        self.release_date = release_date


class GameInfo(db.Model):
    __tablename__ = "game_info"

    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), primary_key=True)
    game = db.relationship("Game", back_populates="info")

    description = db.Column(db.Text, nullable=True)

    def __init__(self, description=None):
        self.description = description
