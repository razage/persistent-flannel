import json

from sqlalchemy_utils import Currency

from pf import db
from pf.companies.models import Company
from pf.games.models import Game, GameInfo, GamePrice
from pf.tags.models import Tag, TagType
from pf.users.models import User, UserLevel

userlevel_map = [UserLevel.STANDARD, UserLevel.MOD, UserLevel.ADMIN, UserLevel.SUPERADMIN]
tagtype_map = {'Genre': TagType.GENERIC, 'Generic': TagType.GENERIC, 'Technical': TagType.TECHNICAL}


def populate_db():
    raw_data = json.load(open("initial_data.json"))

    db.session.close()
    db.drop_all()
    db.create_all()
    db.session.commit()

    for user in raw_data['users'].items():
        u = User(user[0], user[1]['password'], user[1]['email'])
        u.level = userlevel_map[user[1]['level']]
        db.session.add(u)

    db.session.commit()

    for tag in raw_data['tags'].items():
        t = Tag(tag[0], tagtype_map[tag[1]])
        db.session.add(t)

    db.session.commit()

    for company in raw_data['companies'].items():
        c = Company(company[0])
        c.founding_date = None if company[1]['founding_date'] == '' else company[1]['founding_date']

        db.session.add(c)

    db.session.commit()

    for game in raw_data['games'].items():
        g = Game(game[0])
        gi = GameInfo(game[1]['info']['release_date'], game[1]['info']['description'])

        g.info = gi

        try:
            for price in game[1]['prices']:
                p = GamePrice( price['amount'], Currency(price['currency']))
                g.prices.append(p)
        except KeyError:
            pass

        for dev in game[1]['developers']:
            d = Company.by_name(dev)
            g.developers.append(d)

        for pub in game[1]['publishers']:
            p = Company.by_name(pub)
            g.publishers.append(p)

        for tag in game[1]['tags']:
            t = Tag.by_name(tag)
            g.tags.append(t)

        db.session.add(g)

    db.session.commit()

if __name__ == "__main__":
    populate_db()
