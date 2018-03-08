from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^register/$', views.register),
	url(r'^login/$', views.user_login),
	url(r'^logout/$', views.user_logout),
	url(r'^contentupload/$', views.contentupload),
	url(r'^markerdownload/$', views.markerdownload),
]