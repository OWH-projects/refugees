from django.conf.urls import *

urlpatterns = patterns('',
    (r'^', 'myproject.refugees.views.Main'),
    )