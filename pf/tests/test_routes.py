import os
from tempfile import mkstemp
from unittest import TestCase

from pf import app, db


class RouteTestCase(TestCase):

    def setUp(self):
        self.db, app.config['DATABASE'] = mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        os.close(self.db)
        os.unlink(app.config['DATABASE'])

    def test_index(self):
        rv = self.app.get('/')
        assert rv.status == "200 OK"
