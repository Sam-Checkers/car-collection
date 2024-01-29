from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, equal_to

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    first_name = StringField('First_name', validators=[DataRequired(), Length(max=20)])
    last_name = StringField('Last_name', validators=[DataRequired(), Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), equal_to('Password')])
    submit = SubmitField('Sign up!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')