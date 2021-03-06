from django.conf.urls import url
from . import views
from django.conf.urls import url
from . import views

app_name = 'dfy_django'

urlpatterns = [
    url('^index/$', views.index, name='index'),
    # url('^article/(?P<article_id>[0-9]+)$', views.article_page),
    url('^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url('^article/edit$', views.article_edit_page, name='article_edit_page'),
    url('^article/edit/action$', views.article_edit_page_action, name='article_edit_page_action')
]
