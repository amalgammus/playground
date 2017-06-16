from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clients_list, name='clients_list'),
    url(r'^client/(?P<pk>[0-9]+)/$', views.client_detail, name='client_detail'),
]
