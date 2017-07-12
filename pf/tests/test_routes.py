import os
import unittest

from flask import g

from create_examples import populate_db
from pf import app, db


class RouteTestCase(unittest.TestCase):

    def setUp(self):
        if not os.environ.get("TRAVIS"):
            app.config.from_object('config-test')
        else:
            app.config.from_object('config')
            app.config['WTF_CSRF_ENABLED'] = False

        app.config['TESTING'] = True
        self.app = app.test_client()

        with app.app_context():
            db.create_all()
            populate_db()

    def test_index(self):
        rv = self.app.get('/')
        assert rv.status == "200 OK"

    def test_game_view(self):
        with app.app_context():
            rv = self.app.get('/games/1')
            rv2 = self.app.get('/games/200')

            assert rv.status == "200 OK"
            assert rv2.status == "404 NOT FOUND"

    def test_login(self):
        with app.app_context():
            rv = self.app.post('/users/login', data=dict(username="testuser", password="password"))

            assert rv.status == "200 OK"
            assert g.user is not None
            assert g.user.username == "testuser"

    def test_logout(self):
        with app.app_context():
            rv = self.app.post('/users/login', data=dict(username="testuser", password="password"))
            assert rv.status == "200 OK"
            assert g.user is not None

            rv = self.app.get('/users/logout')
            assert rv.status == "302 FOUND"
            assert g.user is None

if __name__ == '__main__':
    unittest.main()
