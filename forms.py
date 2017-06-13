from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)
from flask_wtf import FlaskForm as Form
from database_service import db_session

from models import User
db = db_session()

def name_exists(form, field):
    if db.query(User).filter_by(user_name=field.data).first():
        raise ValidationError('User with that name already exists.')

def email_exists(form, field):
    if db.query(User).filter_by(user_email=field.data).first():
        raise ValidationError('User with that email already exists.')


class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[DataRequired(), Regexp(r'^[a-zA-Z0-9_]+$',
                                           message=("Username should be one word, letters, numbers, and underscores only.")),
                    name_exists])
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), email_exists])

    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=2), EqualTo('password2', message='Passwords must match')])

    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired()])


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remeber_me = BooleanField('Remember_Me', default=False)


class PostForm(Form):
    content = TextAreaField("What's up?", validators=[DataRequired()])


class CharacterForm(Form):
    char_name = StringField('Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    sex = StringField('Sex', validators=[DataRequired()])
    faction = StringField('Faction', validators=[DataRequired()])
    alg = StringField('ALG', validators=[DataRequired()])
    pocc = StringField('POCC', validators=[DataRequired()])
    socc = StringField('SOCC', validators=[DataRequired()])
    hp = StringField('HP', validators=[DataRequired(), Regexp(r'^[0-9]+$', message=("Numbers Only"))])
    str = StringField('STR', validators=[DataRequired(), Regexp(r'^[0-9]+$', message=("Numbers Only"))])
    int = StringField('INT', validators=[DataRequired(), Regexp(r'^[0-9]+$', message=("Numbers Only"))])
    dex = StringField('DEX', validators=[DataRequired(), Regexp(r'^[0-9]+$', message=("Numbers Only"))])
    con = StringField('CON', validators=[DataRequired(), Regexp(r'^[0-9]+$', message=("Numbers Only"))])
    wis = StringField('WIS', validators=[DataRequired(), Regexp(r'^[0-9]+$', message=("Numbers Only"))])
    cha = StringField('CHA', validators=[DataRequired(), Regexp(r'^[0-9]+$', message=("Numbers Only"))])
    merits = StringField('Merits', validators=[DataRequired()])
    flaws = StringField('Flaws', validators=[DataRequired()])
