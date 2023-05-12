from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=2550)
    genre = models.ManyToManyField(Genre)
    num_of_reviews = models.IntegerField(max_length=255)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Мертв', null=True, blank=True)
    inf_about = models.TextField(max_length=2550)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
