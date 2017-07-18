from pf import db
from pf.companies.models import Company
from pf.games.models import Game, GameInfo, GamePrice
from pf.tags.models import Tag
from pf.users.models import User

db.create_all()
db.session.commit()
