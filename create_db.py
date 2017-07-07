from pf import db
from pf.companies.models import Company
from pf.games.models import Game, GameInfo
from pf.tags.models import Tag

db.create_all()
db.session.commit()
