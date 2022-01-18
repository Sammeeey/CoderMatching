from django.urls import path

from . import views

app_name = 'codermatch'
urlpatterns = [
    path('', views.index, name='index'),
    path('ad-search/', views.adSearch, name='adSearch'),
    path('ad-detail/<int:adId>/', views.detail, name='adDetail'),
    path('create-ad/', views.createAd, name='createAd'),
    # path('test-templating/', views.testTemplating, name='testTemplating'),
    # path('test-templating<int:numArg>/', views.testTemplating, name='testTemplating'),
    # path('<int:adId>/vote/', views.vote, name='vote'),
]