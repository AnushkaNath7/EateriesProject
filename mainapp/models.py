from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    image = models.ImageField()
    tag = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class BackgroundNav(models.Model):
    image = models.ImageField()

    def __str__(self):
        return 'NavBAckground'+str(self.id)
