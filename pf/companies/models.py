from pf import db
from pf.models import BaseModel


class Company(BaseModel):
    __tablename__ = "companies"
    name = db.Column(db.String(32), unique=True)

    def __init__(self, name):
        self.name = name
