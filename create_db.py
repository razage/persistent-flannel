from pf import db
from pf.companies.models import Company
from pf.games.models import Game, GameInfo

db.create_all()
db.session.commit()
