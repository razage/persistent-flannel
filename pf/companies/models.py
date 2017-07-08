from pf import db
from pf.models import BaseModel


class Company(BaseModel):
    __tablename__ = "companies"
    name = db.Column(db.String(32), unique=True)
    founding_date = db.Column(db.Date, nullable=True)

    developed_games = db.relationship('Game', secondary="assoc_game_developers", back_populates="developers")
    published_games = db.relationship('Game', secondary="assoc_game_publishers", back_populates="publishers")

    def __init__(self, name, founding_date=None):
        self.name = name
        self.founding_date = founding_date
