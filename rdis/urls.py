from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rdis.views.home', name='home'),
    url(r'^data_manager/', include('data_manager.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
