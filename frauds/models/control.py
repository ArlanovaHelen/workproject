from django.db import models


class Control(models.Model):
    num = models.CharField(max_length=220)
    description = models.CharField(max_length=220)

    def __str__(self):
        return self.name
