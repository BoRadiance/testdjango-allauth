from django.urls import re_path
from . import views

app_name = "app01"
urlpatterns = [
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^profile/update/$', views.profile_update, name='profile_update'),
]