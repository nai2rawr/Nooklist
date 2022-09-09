from django.db import models

# Create your models here.
class Houseware(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

        def __str__(self):
            return self.name


class Clothing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Villager(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Resources(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bid price = models.CharField(max_length=250)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name
