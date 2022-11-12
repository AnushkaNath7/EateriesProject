from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    image = models.ImageField()
    tag = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20000)
    # description = models.CharField(max_length=20000)
    price = models.IntegerField(default=0)
    restaurant = models.CharField(default="", max_length=2000)
    type = models.IntegerField(default=1)
    # 0 for starter,1 for main course, 2 for dessert
    # image = models.ImageField()
    # tag = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class BackgroundNav(models.Model):
    image = models.ImageField()

    def __str__(self):
        return 'NavBAckground'+str(self.id)
