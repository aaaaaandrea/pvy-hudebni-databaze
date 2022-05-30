from django.urls import path
from databaze import views

urlpatterns = [
    path('', views.index, name='index'),
]