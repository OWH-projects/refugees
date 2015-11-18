from django.conf.urls import *

urlpatterns = patterns('',
    (r'^/state/(?P<st>\w{2})$', 'refugees.views.State'),
    (r'^/country/(?P<country>[0-9]{3})$', 'refugees.views.Country'),
    (r'^/about$', 'refugees.views.About'),
    (r'^', 'refugees.views.Main'),
    )