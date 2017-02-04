from django.conf.urls import url

from . import views

app_name = 'bookmarker'
urlpatterns = [
    url(r'^login/?$', views.login_view, name='login'),
    url(r'^signup/?$', views.signup, name='signup'),

    url(r'^$', views.index, name='index'),
    url(r'^users/?$', views.users, name='users'),
    url(r'^(?P<bookmark_id>[0-9A-z]+)/?$', views.edit, name='edit'),
]