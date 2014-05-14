from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from ContactsApp.views import *

admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', profile),
	
	url(r'^$', frontPage),
	url(r'^new_contact/$', newContact),
	url(r'^edit_contact/$', editContact),
	url(r'^delete_contact/$', deleteContact),
	url(r'^save_contact$', saveContact),
    url(r'^admin/',  include(admin.site.urls))
)
