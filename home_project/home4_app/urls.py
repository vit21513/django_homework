from django.urls import path
from . import views

urlpatterns = [
    path('/creaty_product/', views.creaty_product, name='creaty_product'),
    path('/add_photo/', views.add_photo, name='add_photo'),

]
