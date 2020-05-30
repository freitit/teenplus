from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/increase', views.increaseActionNumber, name='increaseActionNumber'),
    path('ajax', views.getActionNumber, name='getActionNumber')
]