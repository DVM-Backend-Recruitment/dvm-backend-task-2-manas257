from django.urls import path
from . import views


urlpatterns=[

  path('', views.home, name='blog-home'),
  path('Search/', views.search, name='movie-search'),
  
  
]