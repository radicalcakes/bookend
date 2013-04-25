from wtforms import Form, BooleanField, TextField, PasswordField, DateTimeField, PasswordField, \
	RadioField, SelectField, SubmitField, HiddenField, IntegerField, validators
from wtforms.validators import ValidationError
from wtforms.widgets import PasswordInput

from flask_peewee.utils import make_password, check_password

from auth import auth

from models import User


class LoginForm(Form):
	username = TextField([validators.Length(min=4, max=70)],
		description="Username")
	password = PasswordField([validators.Length(min=6)], description="Password",
		widget=PasswordInput())


class RegisterForm(Form):
	register_username = TextField([validators.Length(min=4, max=25)])
	email = TextField([validators.Length(min=6, max=35)])
	register_password = PasswordField([
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
	confirm = PasswordField()


class AddressForm(Form):
	street = TextField()
	zipcode = IntegerField()
	state = TextField()
	country = TextField()


class BookForm(Form):
	title = TextField()
	author = TextField()
	isbn = TextField()


		



