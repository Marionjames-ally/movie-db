from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


def validate_email(data_field):
    if User.query.filter_by(email=data_field.data).first():
        raise ValidationError('There is an account with that email')


def validate_username(data_field):
    if User.query.filter_by(username=data_field.data).first():
        raise ValidationError('That username is taken')


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[DataRequired(), Email()])
    username = StringField('Enter your username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Passwords', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
