from django.shortcuts import render
from .models import Movie
from django.shortcuts import render,get_object_or_404
from datetime import datetime,timedelta
from movies.views import oppenheimer


def home(request):
    content={
        'movies':Movie.objects.all()
    }
    
    return render(request, 'blog/home.html',content)

def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        movies2=Movie.objects.filter(title__icontains=searched)
    return render(request,'blog/search.html',{'searched':searched,'movies2':movies2})











    

