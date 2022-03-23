from django.urls import path

from . import views
from .views import AdDetailView

app_name = 'codermatch'
urlpatterns = [
    path('', views.index, name='index'),
    path('ad-search/', views.adSearch, name='adSearch'),
    path('ad-detail/<int:pk>/', AdDetailView.as_view(), name='adDetail'),
    path('create-ad/', views.createAd, name='createAd'),
    path('how-to-codermatching/', views.howToCoderMatching, name='howToCM'),
]