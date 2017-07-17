from datetime import datetime, timedelta

from flask import Blueprint, g, jsonify, make_response, request, session
from flask_restful import Api, Resource

from pf import app, db
from .models import User
from .schemas import UserSchema


mod = Blueprint("users", __name__, url_prefix="/users")
api = Api(mod)


@app.before_request
def before_request():
    g.user = None

    if 'uid' in session:
        user = User.by_id(session['uid'])

        if not user:
            return logout()

        g.user = user


@mod.route("/logout")
def logout():
    if g.user is not None:
        g.user = None
        session.permanent = False
        session.modified = False

        response = make_response(jsonify(success="You have been logged out."), 200)
        response.set_cookie(app.session_cookie_name, expires=0)
        return response
    else:
        return make_response(jsonify(error="You are not logged in."), 400)


class LoginResource(Resource):
    schema = UserSchema()

    def post(self):
        if g.user:
            return make_response(jsonify(error="You are already logged in."), 400)

        username = request.values.get('username')
        password = request.values.get('password')
        remember = request.values.get('remember')
        user = User.by_username(username)

        if not user or password != user.password_hash or not user.is_active:
            return make_response(jsonify(error="Invalid username or password."), 400)

        user.last_login_date = datetime.utcnow()
        db.session.add(user)
        db.session.commit()

        g.user = user
        session['uid'] = user.id
        session['uname'] = user.username

        if remember == "true":
            session.permanent = True
            session.modified = True

        return self.schema.jsonify(user)


api.add_resource(LoginResource, "/login")
