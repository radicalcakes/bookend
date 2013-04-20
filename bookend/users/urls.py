from django.conf import settings
from django.conf.urls import patterns, include, url
from users.views import Home

urlpatterns = patterns('',
	#url(r'join/$', 'users.views.registration', name="join"),
	#url(r'login/$', 'users.views.login', name="login"),
	#url(r'logout/$', 'users.views.logout', name="logout")
)