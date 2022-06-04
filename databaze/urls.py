from django.urls import path
from databaze import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', views.AlbumListView.as_view(), name='album_list'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail')
]