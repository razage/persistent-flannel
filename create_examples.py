from pf import db
from pf.companies.models import Company
from pf.games.models import Game, GameInfo
from pf.tags.models import Tag
from pf.users.models import User

companies = ("NEKO WORKs", "Sekai Project", "Square Enix", "Frontwing", "Ludeon Studios", "Re-Logic", "ConcernedApe",
             "Chucklefish", "Marvelous", "HONEY∞PARADE GAMES", "Meteorise")
company_objs = {}

games = ("NEKOPARA Vol. 3", "Terraria", "RimWorld", "FINAL FANTASY XIV Online", "Stardew Valley",
         "The Fruit of Grisaia", "NieR:Automata", "VALKYRIE DRIVE -BHIKKHUNI-")
game_objs = {}


# I'm using this function to test various things related to the database. This will not be used to initialize the db.
def populate_db():
    # Clean up any old data
    db.session.close()
    db.drop_all()
    db.create_all()
    db.session.commit()

    for c in companies:
        _c = Company(c)
        company_objs[c] = _c
        db.session.add(_c)

    for g in games:
        _g = Game(g)
        game_objs[g] = _g
        db.session.add(_g)

    db.session.commit()

    game_objs['NEKOPARA Vol. 3'].developers.append(company_objs['NEKO WORKs'])
    game_objs['NEKOPARA Vol. 3'].publishers.append(company_objs['Sekai Project'])

    game_objs['VALKYRIE DRIVE -BHIKKHUNI-'].developers.append(company_objs['Meteorise'])
    game_objs['VALKYRIE DRIVE -BHIKKHUNI-'].developers.append(company_objs['HONEY∞PARADE GAMES'])
    game_objs['VALKYRIE DRIVE -BHIKKHUNI-'].publishers.append(company_objs['Marvelous'])

    db.session.commit()

if __name__ == "__main__":
    populate_db()
