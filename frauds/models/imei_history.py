from django.db import models


class Imei(models.Model):
    imei = models.CharField(max_length=20)
    num_imei = models.CharField(max_length=20)
    # models.SET() add list or set from file
    date_up = models.DateField(verbose_name=None, null=True, blank=True)
    date_to = models.DateField(verbose_name=None, null=True, blank=True)

    def __str__(self):
        return self.imei
