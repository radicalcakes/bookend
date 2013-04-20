from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#abstract base class to allow simpler timestamps
class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

# Create your models here.
class UserProfile(TimeStampedModel):
	#ids are created for us implicitly
	user = models.OneToOneField(User,related_name="profile", unique=True)

	def __unicode__(self):
		return u"%s, %s" % (self.user.username, self.user.email)


class Address(TimeStampedModel):
	pass
