from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^signout/$', views.signout, name='signout'),
]