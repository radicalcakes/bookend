#Database configurations
from flask_pewee.db import Database

from bookend import app

DATABASE = {
	'name': 'radicalcakes',
	'engine': 'peewee.MySQLDatabase',
	
}
