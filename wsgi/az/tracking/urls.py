from django.conf.urls import patterns, url

from tracking import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	
	url(r'^(?P<tracking_number>\w+)/$', views.details, name='details'),
)