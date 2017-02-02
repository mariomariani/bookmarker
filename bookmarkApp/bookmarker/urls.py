from django.conf.urls import url

from . import views

app_name = 'bookmarker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<bookmark_id>[0-9A-z]+)/$', views.edit, name='edit'),
    url(r'^login/?$', views.auth, name='login'),
]