from django.conf.urls import url

from . import views

app_name = 'bookmarker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<bookmark_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login/?$', views.auth, name='login'),
]