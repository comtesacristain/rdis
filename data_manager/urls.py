from django.conf.urls import patterns, url

from data_manager.views import *

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.duplicate, name='duplicate')
)