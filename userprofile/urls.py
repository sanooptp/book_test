from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name= 'users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='userbyone'),
    path('create_user/', views.AddUser.as_view(), name= 'create_user'),
]
