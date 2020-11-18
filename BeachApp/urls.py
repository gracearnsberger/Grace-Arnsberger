from django.contrib import admin
from django.urls import path
from . import views

#url paths for each page

urlpatterns = [
    path('home', views.tropical_cities_home, name='TropicalCitiesHome'),
    path('popular_cities', views.tropical_cities_popular, name='TropicalCitiesPopular'),
    path('save_tropical_cities', views.save_tropical_cities, name='SaveTropicalCities'),
    path('wish_list_index', views.tropical_cities_wish_list_index, name='TropicalCitiesWishList'),
    path('book_hotels', views.tropical_cities_book_hotels, name='TropicalCitiesBookHotels'),
    path('city-details/<int:pk>/', views.tropical_cities_details, name='save_cities'),





]
