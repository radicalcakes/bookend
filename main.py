from app import app, db

from auth import *
from models import *
from views import *

if __name__ == '__main__':
	auth.User.create_table(fail_silently=True)
	Address.create_table(fail_silently=True)
	Books.create_table(fail_silently=True)
	app.run(host= '0.0.0.0', port=1933)