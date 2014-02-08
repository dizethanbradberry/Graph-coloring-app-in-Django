from django.conf.urls import patterns, include, url
from Graphapp.views import home

urlpatterns = patterns('',
    url('^$', home),
)
