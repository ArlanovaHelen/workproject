from django.db import models


class Prison(models.Model):
    name = models.CharField(max_length=220)
    lat = models.CharField(max_length=220)
    lon = models.CharField(max_length=220)
    address = models.CharField(max_length=220)
    oblast = models.CharField(max_length=220)

    def __str__(self):
        return self.name
