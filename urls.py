from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.index_view, name='chat-index'),
    path('auth/', views.auth, name='auth'),
    path('<str:room_name>/', views.room_view, name='chat-room'),
]
