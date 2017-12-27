from django.conf.urls import url
from . import views
from django.conf.urls import url
from . import views

app_neme = 'dfy_django'

urlpatterns = [
    url('^index/$', views.index),
]
