from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
]