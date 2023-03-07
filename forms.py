from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, DecimalField, DateField
from wtforms.validators import InputRequired, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username: ", 
                            validators=[InputRequired()]
                           )
    password = PasswordField("Password: ", 
                            validators=[InputRequired()]
                            )
    password2 = PasswordField("Confirm Password: ", 
                            validators=[InputRequired(), EqualTo("password")]
                            )
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("Username:", 
                            validators=[InputRequired()]
                           )
    password = PasswordField("Password:", 
                            validators=[InputRequired()]
                            )
    submit = SubmitField("Submit")

class CheckoutForm(FlaskForm):
    name = StringField("Name:",
                            validators=[InputRequired()])
    submit = SubmitField("Submit")

# Admin Dashboard Forms
class AddNewsForm(FlaskForm):
    title = StringField("Title:",
                            validators=[InputRequired()])
    content = StringField("Content:",
                            validators=[InputRequired()])
    submit1 = SubmitField("Submit")

class AddTournamentForm(FlaskForm):
    name = StringField("Name:",
                            validators=[InputRequired()])
    date = DateField("Date:",
                            validators=[InputRequired()])
    start_time = StringField("Start Time:",
                            validators=[InputRequired()])
    entry_fee = DecimalField("Entry Fee:",
                            validators=[InputRequired()])
    prize_money = DecimalField("Prize Money:",
                            validators=[InputRequired()])
    description = StringField("Description:",
                            validators=[InputRequired()])
    submit2 = SubmitField("Submit")