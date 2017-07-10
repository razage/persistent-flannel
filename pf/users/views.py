from datetime import datetime, timedelta

from flask import Blueprint, flash, g, Markup, make_response, redirect, render_template, request, session, url_for

from pf import app, db
from .forms import LoginForm
from .models import User, UserStatus


mod = Blueprint("users", __name__, url_prefix="/users")


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


# Don't actually render anything; this will just be used to log in...eventually
@mod.route("/login", methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for("home"))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data.strip()
        password = form.password.data
        user = User.by_username(username)

        if not user or password != user.password_hash or not user.is_active:
            flash(Markup('<strong>Login failed!</strong> Incorrect username or password.'), 'danger')
            return redirect(url_for('login'))

        user.last_login_date = datetime.utcnow()
        db.session.add(user)
        db.session.commit()

        g.user = user
        session['user_id'] = user.id
        session.permanent = True
        session.modified = True

        return redirect(url_for("home"))

    return render_template('users/login.html', title="Login", form=form)


@mod.route("/logout")
def logout():
    g.user = None
    session.permanent = False
    session.modified = False

    response = make_response(redirect(url_for("home")))
    response.set_cookie(app.session_cookie_name, expires=0)
    return response
