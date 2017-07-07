from pf import db
from pf.models import BaseModel


class Tag(BaseModel):
    __tablename__ = "tags"

    name = db.Column(db.String(32), unique=True)

    def __init__(self, name):
        self.name = name
