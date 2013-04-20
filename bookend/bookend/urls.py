from django.conf.urls import patterns, include, url
#use class based views instead as_view()
from users.views import Home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:    
    url(r'^$', Home.as_view(),name='home'),
    url(r'^user/', include('users.urls')),
    # url(r'^bookend/', include('bookend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
