import datetime

from flask_peewee.auth import BaseUser
from peewee import *

from app import db

#User Object which will be executed as a table in app.py
class User(db.Model, BaseUser):
	username = CharField()
	email = CharField()
	password = CharField()
	creation_date = DateTimeField(default=datetime.datetime.now)
	active = BooleanField(default=True)

	def __unicode__(self):
		return self.username


class Address(db.Model):
	user = ForeignKeyField(User, related_name="address")
	street = TextField()
	zipcode = IntegerField()
	state = TextField()
	country = TextField()



#utility model to help with finding inter-user relationships
#ie; shipper to sender and vice versa
class Relationship(db.Model):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')

    def __unicode__(self):
        return 'Relationship from %s to %s' % (self.from_user, self.to_user)


class Books(db.Model):
	ownership = ForeignKeyField(User, related_name="book")
	title = CharField(null=False)
	author = CharField()
	isbn = TextField()
	
	def __unicode__(self):
		return self.title, self.author