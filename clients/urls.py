from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clients_list, name='clients_list'),
]
