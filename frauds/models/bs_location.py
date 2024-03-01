from django.db import models


class BSLocation(models.Model):
    address = models.CharField(max_length=270, null=True, blank=True)
    LAC = models.CharField(max_length=270)
    SID = models.IntegerField(null=True, blank=True)
    AZ = models.IntegerField(null=True, blank=True)
    lat = models.CharField(max_length=100, null=True, blank=True)
    lon = models.CharField(max_length=100, null=True, blank=True)
    oblast = models.CharField(max_length=220, null=True, blank=True)

    def __str__(self):
        return self.name
