from django.contrib import admin 
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views 
  


urlpatterns = [ 
    path('menu-items/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/',views.SingleMenuItemView.as_view(), name='single-menu-items'),
    path('api-token-auth/', obtain_auth_token)
]