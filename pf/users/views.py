from datetime import datetime

from flask import Blueprint, flash, g, Markup, redirect, render_template, request, url_for

from pf import db
from .forms import LoginForm
from .models import User


mod = Blueprint("users", __name__, url_prefix="/users")


# Don't actually render anything, this will just be used to log in
@mod.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == "POST":
        username = form.username.data.strip()
        password = form.password.data
        user = User.by_username(username)

        if not user or password != user.password_hash or not user.is_active:
            flash(Markup('<strong>Login failed!</strong> Incorrect username or password.'), 'danger')
            return redirect(url_for("users.login"))

        user.last_login_date = datetime.utcnow()
        db.session.add(user)
        g.user = user

        flash(Markup('<strong>Login Successful!</strong> Welcome Back %s' % user.username), 'success')

        return redirect(url_for("home"))

    return render_template("users/login.html", title="Login", form=form)
