"""Forms module of 'users' package."""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):  # type: ignore
    """A class for a regitration form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    role = RadioField('Role', choices=[('student', 'Estudiante'), ('teacher', 'Profesor')], default='student', validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):  # type: ignore
    """A class for a login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")
