from django.conf.urls import *

urlpatterns = patterns('',
    (r'^/state/(?P<st>\w{2})$', 'myproject.refugees.views.State'),
    (r'^/country/(?P<country>[0-9]{3})$', 'myproject.refugees.views.Country'),
    (r'^', 'myproject.refugees.views.Main'),
    )