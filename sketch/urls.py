from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Equipment/', views.Equipment, name='equipment'),
    path('money/', views.money, name='money'),
    path('renew/', views.renew, name='renew'),
    path('team/', views.team, name='team'),
]