from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class Film(models.Model):
    # CHOICES = (
    #     (1, 'dupa'),
    #     (2, 'mala dupa'),
    #     (3, 'dobry'),
    #     (4, 'super dupas'),
    #
    # )
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed')
    screenwriter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='written')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # ranking = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return f"{self.title} {self.year}"