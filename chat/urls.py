from django.urls import path
from . import views


urlpatterns = [
    path('', views.chat_view),
    path('<str:room_name>/', views.room_view),
    ]