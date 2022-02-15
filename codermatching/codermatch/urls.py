from django.urls import path

from . import views

app_name = 'codermatch'
urlpatterns = [
    path('', views.index, name='index'),
    path('ad-search/', views.adSearch, name='adSearch'),
    path('ad-detail/<int:adId>/', views.detail, name='adDetail'),
    path('create-ad/', views.createAd, name='createAd'),
]