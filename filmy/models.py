from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

class Category(models.Model):
    name = models.CharField(max_length=125)
    #film_set

class Film(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed')
    screenwriter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='written')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)