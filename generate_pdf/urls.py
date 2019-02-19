from django.contrib import admin
from django.conf.urls import url,include
from .import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^get_json/$', views.get_json),
    url(r'^get_pdf/$', views.get_pdf),

]