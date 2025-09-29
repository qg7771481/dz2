from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class TorontoTokyo(models.Model):
    name = models.CharField(max_length=111)
    description = models.TextField(blank=False)
    how_many_games_on_beastmaster = models.IntegerField(max_length=300)
    city_Toronto = models.IntegerField(max_length=322)
    prize = models.IntegerField(max_length=30)
    city_Tokyo = models.CharField(max_length=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)




    def __str__(self):
        return self.name