from datetime import datetime, timedelta

from flask import Blueprint, g, jsonify, make_response, redirect, request, session, url_for
from flask_restful import Api, Resource

from pf import app, db
from .models import User
from .schemas import UserSchema


mod = Blueprint("users", __name__, url_prefix="/users")
api = Api(mod)


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = User.by_id(session['user_id'])

        if not user:
            return logout()

        g.user = user

        if 'timeout' not in session or session['timeout'] < datetime.now():
            session['timeout'] = datetime.now() + timedelta(days=7)
            session.permanent = True
            session.modified = True


@mod.route("/logout")
def logout():
    g.user = None
    session.permanent = False
    session.modified = False

    response = make_response(redirect(url_for("home")))
    response.set_cookie(app.session_cookie_name, expires=0)
    return response


class LoginResource(Resource):
    schema = UserSchema()

    def post(self):
        if g.user:
            return make_response(jsonify(error="You are already logged in."), 400)

        username = request.values.get('username')
        password = request.values.get('password')
        user = User.by_username(username)

        if not user or password != user.password_hash or not user.is_active:
            return make_response(jsonify(error="Invalid username or password."), 400)

        user.last_login_date = datetime.utcnow()
        db.session.add(user)
        db.session.commit()

        g.user = user
        session['user_id'] = user.id
        session.permanent = True
        session.modified = True

        return self.schema.jsonify(user)


api.add_resource(LoginResource, "/login")
