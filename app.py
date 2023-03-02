'''



'''

from flask import Flask, render_template, session, redirect, url_for, g, request
from database import get_db, close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from functools import wraps

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def logged_in_user():
    g.user = session.get("username", None)

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(*args, **kwargs)
    return wrapped_view

@app.route("/")
def index():
    db = get_db()
    news = db.execute("""SELECT * FROM news ORDER BY blog_id DESC;""").fetchall()
    return render_template("index.html", news=news)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users
                                               WHERE username = ?;""", (username,)).fetchone()
        if possible_clashing_user is not None:
            form.username.errors.append("Username is already taken!")
        else:
            db.execute("""INSERT INTO users (username, password, is_admin)
                          VALUES (?, ?, 0);""", (username, generate_password_hash(password)))
            db.commit()
            return redirect( url_for("login") )
    return render_template("register.html", form=form)

@app.route("/store")
def store():
    db = get_db()
    tournaments = db.execute("""SELECT * FROM tournaments
                                WHERE date >= date('now');""").fetchall()
    return render_template("store.html", tournaments=tournaments)

@app.route("/database")
def database():
    db = get_db()
    tournaments = db.execute("""SELECT * FROM tournaments;""").fetchall()
    return render_template("database.html", tournaments=tournaments)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users
                                               WHERE username = ?;""", (username,)).fetchone()
        if possible_clashing_user is None:
            form.username.errors.append("Username is not registered!")
        elif not check_password_hash(possible_clashing_user["password"], password):
            form.password.errors.append("Password is incorrect!")
        else:
            session.clear()
            session["username"] = username
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("login.html", form=form)