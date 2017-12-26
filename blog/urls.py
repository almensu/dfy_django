from django.conf.urls import url
from . import views
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index/$', views.index),
    # url('^article/(?P<article_id>[0-9]+)$', views.article_page),
    url('^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
]
