from django.conf.urls import url

from . import views

app_name = 'bookmarker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<bookmark_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<bookmark_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<bookmark_id>[0-9]+)/vote/$', views.vote, name='vote'),
]