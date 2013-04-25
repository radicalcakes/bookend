import datetime

from flask import request, redirect, url_for, render_template, flash, render_template_string

from flask_peewee.utils import get_object_or_404, object_list, make_password, check_password

from app import app
from auth import auth
from models import User, Relationship, Address, Books
from forms import LoginForm, RegisterForm, AddressForm, BookForm



@app.route('/', methods=["GET", "POST"])
def homepage():
	login_form = LoginForm(request.form)
	register_form = RegisterForm(request.form)
	login_errors = ""
	register_errors = ""
	if request.method == "POST":
		if login_form.username.name in request.form and login_form.validate():
			try:
				#makes a select query here to see if username post data is in database
				user = User.select().where(User.username==request.form['username']).get()
				if check_password(request.form["username"],
					make_password(request.form["username"])):
						auth.login_user(user)
						return redirect(url_for("dashboard"))
			except User.DoesNotExist:
				login_errors = "This User does not exist"
				return render_template("home.html", login_form=login_form, login_errors=login_errors, register_form=register_form, register_errors=register_errors)
		elif register_form.register_username.name in request.form and register_form.validate():			
			try:
				exists = User.select().where(User.username==request.form["register_username"]).get()
				register_errors= "Sorry, %s has been taken." % (request.form["register_username"])
				return render_template("home.html", login_form=login_form, login_errors=login_errors, register_form=register_form, register_errors=register_errors)
			except User.DoesNotExist:
				if register_form.register_password.data != register_form.confirm.data:
					register_errors= "Passwords do not match"
					return render_template("home.html", login_form=login_form, login_errors=login_errors, register_form=register_form, register_errors=register_errors)
				else:
					u = User(
						username=register_form.register_username.data,
						email=register_form.email.data,
						creation_date=datetime.datetime.now(),
						active=True
						)
					u.set_password(register_form.register_password.data)
					u.save()
					auth.login_user(u)
					return redirect(url_for("dashboard"))
	else:
		return render_template("home.html", login_form=login_form, login_errors=login_errors, register_form=register_form, register_errors=register_errors)


@app.route("/dashboard", methods=["GET", "POST"])
@auth.login_required
def dashboard(msg=None):
	user = auth.get_logged_in_user()
	try:
		books = Books.select().where(
			Books.ownership == user).order_by(Books.id.desc())
		return object_list("book_list.html", books, 'book_list')
	except Books.DoesNotExist:
		return render_template("dashboard.html", msg=msg)
	return render_template("dashboard.html", msg=msg)

@app.route("/logout")
def logout():
	auth.logout_user(auth.get_logged_in_user())
	return redirect(url_for("homepage"))

@app.route("/address_create", methods=["GET", "POST"])
@auth.login_required
def address_create():
	address_form = AddressForm(request.form)
	user = auth.get_logged_in_user()
	if request.method == "POST":
		address = Address(
			user = user,
			street=address_form.street.data,
			zipcode=address_form.zipcode.data,
			state=address_form.state.data,
			country=address_form.country.data
			)
		address.save()
		flash("Address successfully saved")
		return redirect(url_for("dashboard"))
	elif request.method == "GET":
		try:
			exist = Address.select().where(Address.user == user).get()
			return redirect(url_for("address"))
		except Address.DoesNotExist:
			if request.method == "POST":
				address = Address(
					user = user,
					street=address_form.street.data,
					zipcode=address_form.zipcode.data,
					state=address_form.state.data,
					country=address_form.country.data
					)
				address.save()
				flash("Address successfully saved")
				return redirect(url_for("dashboard"))
			else:
				return render_template("address_create.html", address_form=address_form)


@app.route("/address_edit", methods=["GET", "POST"])
@auth.login_required
def address():
	address_form = AddressForm(request.form)
	user = auth.get_logged_in_user()
	address = get_object_or_404(Address, Address.user == user)
	if request.method == "POST":
		address = address.update(
			street=request.form["street"],
			zipcode=request.form["zipcode"],
			state=request.form["state"],
			country=request.form["country"]).where(address.user == user)
		address.execute()
		flash("Address successfully saved")
		return redirect(url_for("dashboard"))
	elif request.method =="GET":
		street = address.street
		zipcode = address.zipcode
		state = address.state
		country = address.country
		return render_template("address.html", street=street, zipcode=zipcode, state=state, country=country, address_form=address_form)

@app.route("/book_add", methods=["GET", "POST"])
@auth.login_required
def book_add(msg = ""):
	book_form = BookForm(request.form)
	user = auth.get_logged_in_user()
	if request.method == "POST":
		books = Books(
			ownership = user,
			title = book_form.title.data,
			author = book_form.author.data,
			isbn = book_form.isbn.data,
		)
		books.save()
		flash("Book successfully saved")
		msg = "Book successfully saved"
		book_form = BookForm()
		return render_template("book_add.html", book_form=book_form, msg=msg)
	else:
		return render_template("book_add.html", book_form=book_form, msg=msg)		


@app.route("/shipped", methods=["GET", "POST"])
@auth.login_required
def ship():
	user = auth.get_logged_in_user()
	#book = get_object_or_404(Books, Books.user == user, Books.id)
	if request.method == "POST":
		book_id = request.form["book_id"]
		b = Books.delete().where(Books.ownership == user and Books.id == book_id)
		b.execute()
		return render_template("shipped.html")
	else:
		print "wtf"
		return redirect(url_for("dashboard"))