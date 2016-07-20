from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.calculate_total, name='calculate_total')
]
