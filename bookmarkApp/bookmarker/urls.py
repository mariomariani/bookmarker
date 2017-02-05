from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'bookmarker'
urlpatterns = [
    url(r'^login/?$', views.login_view, name='login'),
    url(r'^signup/?$', views.signup, name='signup'),

    url(r'^$', RedirectView.as_view(url='bookmarks')),
    url(r'^users/?$', views.users, name='users'),
    url(r'^bookmarks/?$', views.index, name='index'),
    url(r'^bookmarks/(?P<bookmark_id>[0-9A-z]+)/?$', views.edit, name='edit'),
]
