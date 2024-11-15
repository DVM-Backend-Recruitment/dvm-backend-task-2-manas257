from django.urls import path
from . import views

app_name='movies'
urlpatterns=[

  path('<slug:slug>/', views.movie_details ,name='movie-details'),
  
 
  
]