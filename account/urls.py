from django.conf.urls import url

from . import views

app_name = 'account'

urlpatterns = [
    url('sign_up', views.sign_up),
    url('sign_in', views.sign_in),
    url('sign_out', views.sign_out),
    url('search', views.search),
    url('', views.index),
]
