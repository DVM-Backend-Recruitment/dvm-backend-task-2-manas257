from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify


class Movie(models.Model):
    title = models.CharField(max_length=100)
    Director = models.CharField(max_length=100)
    Ratings=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    slug=models.SlugField()

    def __str__(self):
       return self.slug
    

    
    
    
