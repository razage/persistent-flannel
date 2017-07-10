from enum import Enum

from sqlalchemy_utils.types import ChoiceType

from pf import db
from pf.models import BaseModel


class TagType(Enum):
    GENERIC = 0
    GENRE = 1


class Tag(BaseModel):
    __tablename__ = "tags"

    name = db.Column(db.String(32), unique=True, nullable=False)
    tag_type = db.Column(ChoiceType(TagType, impl=db.Integer()), nullable=False)

    games_in_genre = db.relationship('Game', secondary="assoc_game_genres", back_populates="genres")
    games_in_tag = db.relationship('Game', secondary="assoc_game_tags", back_populates="tags")

    def __init__(self, name, tag_type="Generic"):
        self.name = name
        self.tag_type = tag_type

    @property
    def is_genre(self):
        return self.tag_type is TagType.GENRE

    @property
    def is_generic(self):
        return self.tag_type is TagType.GENERIC
