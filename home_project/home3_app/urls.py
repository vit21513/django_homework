from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('/orders/<str:name>/', views.orders_by_user_name, name='orsers_by_user_name'),


]