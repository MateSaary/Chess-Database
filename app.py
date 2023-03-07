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

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

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
    return render_template("register.html", form=form, title="Create Account - Chess Tournaments")

@app.route("/store")
def store():
    db = get_db()
    tournaments = db.execute("""SELECT * FROM tournaments
                                WHERE date >= date('now');""").fetchall()
    return render_template("store.html", tournaments=tournaments, title="Store - Chess Tournaments")

@app.route("/tournament_details/<int:tournament_id>")
def tournament_details(tournament_id):
    db = get_db()
    tournament = db.execute("""SELECT * FROM tournaments
                               WHERE tournament_id = ?;""", (tournament_id,)).fetchone()
    return render_template("tournament_details.html", tournament=tournament, title="Tournament Details - Chess Tournaments")

@app.route("/database")
def database():
    db = get_db()
    tournaments = db.execute("""SELECT * FROM tournaments
                                WHERE date <= date('now');""").fetchall()
    return render_template("database.html", tournaments=tournaments, title="Database - Chess Tournaments")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users
                                               WHERE username = ?;""", (username,)).fetchone()
        possible_admin_user = db.execute("""SELECT * FROM users
                                            WHERE is_admin = 1 AND username = ?;""", (username,)).fetchone()
        if possible_clashing_user is None:
            form.username.errors.append("Username is not registered!")
        elif not check_password_hash(possible_clashing_user["password"], password):
            form.password.errors.append("Password is incorrect!")
        elif possible_admin_user is not None:
            session.clear()
            session["username"] = username
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("admin")
            return redirect(next_page)
        else:
            session.clear()
            session["username"] = username
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("login.html", form=form, title="Login - Chess Tournaments")

@app.route("/cart")
@login_required
def cart():
    if "cart" not in session:
        session["cart"] = {}
    items = {}
    prices = {}
    total = 0
    db = get_db()
    for tournament_id in session["cart"]:
        tournament = db.execute("""SELECT * FROM tournaments
                                   WHERE tournament_id = ?;""", (tournament_id,)).fetchone()
        cost = db.execute("""SELECT entry_fee FROM tournaments
                             WHERE tournament_id = ?;""", (tournament_id,)).fetchone()
        price = tournament["entry_fee"]
        prices[tournament_id] = price
        item = tournament["name"]
        items[tournament_id] = item
        total = sum(prices.values()) 
        #I found this solution to adding up all values in a dictionary here, 
        #specifically the first answer: https://stackoverflow.com/questions/4880960/how-to-sum-all-the-values-in-a-dictionary
    return render_template("cart.html", cart=session["cart"], items=items, prices=prices, total=total, title="Your Cart - Chess Tournaments")

@app.route("/add_to_cart/<int:tournament_id>")
@login_required
def add_to_cart(tournament_id):
    if "cart" not in session:
        session["cart"] = {}
    if tournament_id not in session["cart"]:
        session["cart"][tournament_id] = 1
    else:
        session["cart"][tournament_id] += 1
    return redirect(url_for("cart"))

@app.route("/remove_from_cart/<int:tournament_id>")
@login_required
def remove_from_cart(tournament_id):
    if "cart" not in session:
        session["cart"] = {}
    if tournament_id in session["cart"]:
        del session["cart"][tournament_id]
    return redirect(url_for("cart"))

@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():

    return render_template("checkout.html", title="Checkout - Chess Tournaments")

#Admin Dashboard
@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():

    return render_template("admin.html", title="Admin Dashboard - Chess Tournaments")