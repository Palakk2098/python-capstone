from django.contrib import admin 
from django.urls import path,include
from . import views 
  


urlpatterns = [ 
    path('menu-items/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/',views.SingleMenuItemView.as_view(), name='single-menu-items'),
]