from django.db import models


class Drink(models.Model):
    DoesNotExist = None
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.name
