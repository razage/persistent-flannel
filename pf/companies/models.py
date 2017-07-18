from sqlalchemy_utils.types import URLType

from pf import db
from pf.models import BaseModel


class Company(BaseModel):
    __tablename__ = "companies"
    name = db.Column(db.String(32), unique=True, nullable=False)
    founding_date = db.Column(db.Date)
    website = db.Column(URLType)

    developed_games = db.relationship('Game', secondary="assoc_game_developers", back_populates="developers")
    published_games = db.relationship('Game', secondary="assoc_game_publishers", back_populates="publishers")

    def __init__(self, name, founding_date=None, website=None):
        self.name = name
        self.founding_date = founding_date
        self.website = website

    @classmethod
    def by_name(cls, name):
        company = cls.query.filter_by(name=name).first()
        return company
