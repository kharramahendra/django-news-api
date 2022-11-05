from . import views
from django.urls import path
sports="sports"

urlpatterns = [
    path('', views.home, name="home"),
    path('news/<str:slug>',views.news, name="news"),
    path('news/<str:slug>/<str:slug2>',views.sing_news, name="news"),
    path('search',views.search,name="search"),
    path('weather',views.weather,name="weather"),
    path('about', views.about, name="about"),
]
