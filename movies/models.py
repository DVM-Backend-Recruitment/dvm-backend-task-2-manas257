from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime,timedelta
from blog.models import Movie

def movie_input(self):
    data=Movie.objects.filter(title=self)
    count=0
    movies_title=[]
    for m in data:
        if m.title==self:
            count+=1
            break
        else:
            movies_title+=[m.title]
    if count!=1:
      raise ValidationError(f'Error! Choose A Movie From This List:{movies_title}')



class theater(models.Model):
    movie_title=models.CharField(max_length=100,validators=[movie_input])
    theater_name=models.TextField(max_length=100)
    date=models.DateField(null=True,blank=True )
    time_slot1=models.TimeField()
    time_slot2=models.TimeField()

def theater_name(self):
    data2=theater.objects.filter(title=self)
    count=0
    theater=[]
    for input in data2:
        if input.theater_name==self:
            count+=1
            break
        else:
            theater+=[input.theater_name]
    if count!=1:
      raise ValidationError(f'Error! Choose A Theater From This List:{theater}')

class seats(models.Model):
    theater=models.TextField(max_length=100)
    seat_name1=models.CharField(max_length=100)
    seat_no1=models.IntegerField()
    price1=models.IntegerField(default=200)        
    seat_name2=models.CharField(max_length=100)
    seat_no2=models.IntegerField()
    price2=models.IntegerField(default=200) 
    seat_name3=models.CharField(max_length=100)
    seat_no3=models.IntegerField()
    price3=models.IntegerField(default=200)



   



