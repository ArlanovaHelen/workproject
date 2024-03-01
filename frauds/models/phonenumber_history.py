from django.db import models


class Phonenumber(models.Model):
    number = models.CharField(max_length=20)
    imei_num = models.CharField(max_length=20, null=True, blank=True)
    date_up = models.DateField(verbose_name=None, null=True, blank=True)
    date_to = models.DateField(verbose_name=None, null=True, blank=True)

    def __str__(self):
        return self.number
