from django.conf.urls import url

from . import views

app_name = 'lib'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<id>[0-9]+)/unlike/$', views.unlike, name='unlike'),
    url(r'^(?P<id>[0-9]+)/results$', views.results, name='results'),

]