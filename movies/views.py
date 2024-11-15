from django.shortcuts import render,get_object_or_404
from datetime import datetime,timedelta
from blog.models import Movie
from .models import theater,seats

app_name='movies'

def movie_date(request):
    date1=datetime.now()
    day1=date1.strftime("%d")
    month=date1.strftime("%B")
    date2=date1+ timedelta(days=1)
    day2=date2.strftime("%d")
    date3=date1+ timedelta(days=2)
    day3=date3.strftime("%d")
    content={
        'day1':day1,'day2':day2,'day3':day3,'month':month,
    }
    return content

def movie_details(request,slug):
    movie=get_object_or_404(Movie,slug=slug)
    date1=datetime.now()
    day1=date1.strftime("%d")
    month=date1.strftime("%B")
    date2=date1+ timedelta(days=1)
    day2=date2.strftime("%d")
    date3=date1+ timedelta(days=2)
    day3=date3.strftime("%d")
    data=oppenheimer(request,slug)
    content={
        'day1':day1,'day2':day2,'day3':day3,'month':month,'movie':movie,'data':data,'slug':slug,
    }
    return render(request,'movies/movie_detail.html',content)

def oppenheimer(request,slug):
    movie=get_object_or_404(Movie,slug=slug)
    theater_info=theater.objects.filter(movie_title=movie.title)
    return theater_info

def seat_info(request):
    theater_seats=seats.objects.filter()






