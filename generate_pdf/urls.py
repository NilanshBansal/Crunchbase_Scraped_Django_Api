from django.contrib import admin
from django.conf.urls import url,include
from .import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^get_pdf/$', views.get_pdf),

]