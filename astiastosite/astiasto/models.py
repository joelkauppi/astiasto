from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
#class Order(models.Model):
#    Etunimi = models.CharField(max_length=30)
#    Sukunimi = models.CharField(max_length=40)
#    Sähköposti = models.EmailField()
##    Tapahtuma = models.CharField(max_length=100)
#    Päivänmäärä= models.DateField()
#    Tapahtumapaikka = models.CharField(max_length=100)
#    Määrä = models.IntegerField(default=0)
#    Viesti = models.TextField()


class Genre(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    max_amount = models.IntegerField()
    price_otaniemi = models.FloatField()
    price_others = models.FloatField()
    img = models.ImageField(upload_to='static/img')
    def __str__(self):
        return self.name
