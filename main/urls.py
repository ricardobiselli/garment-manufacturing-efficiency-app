from django.urls import path
from . import views

urlpatterns = [
    path('add_garment/', views.add_garment, name="add_garment"),
    path('select_garment/', views.select_garment, name="select_garment"),
    path('home/', views.home_view, name="home_view"),
    path('start_production/', views.start_production, name="start_production"),
    path('add_garment_success/', views.add_garment_success, name="add_garment_success"),
]
