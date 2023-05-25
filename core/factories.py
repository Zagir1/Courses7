import factory
from faker import Factory
from core import models

factory_ru = Factory.create('ru-Ru')


class TeamFactory(factory.django.DjangoModelFactory):
    name = factory_ru.word()

    class Meta:
        model = models.Genre
