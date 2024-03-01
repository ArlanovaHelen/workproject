from django.db import models
from frauds.models.district import District
from frauds.models.category import Category
from django.core.exceptions import ValidationError


def non_negative_validator(value):
    if value <= 0:
        raise ValidationError("Номер провадження не може бути від'ємним")


class Fraud(models.Model):
    numEO = models.IntegerField(validators=[non_negative_validator], null=True)
    date = models.DateField(verbose_name=None)
    district = models.ForeignKey(
        District,
        on_delete=models.RESTRICT,
        related_name="frauds",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
        related_name="frauds",
        null=True,
        blank=True,
    )
    victim = models.TextField(blank=True)
    numERDR = models.CharField(max_length=15, blank=True, null=True)
    card_number = models.CharField(max_length=30, blank=True, null=True)
    phonenumber = models.CharField(max_length=13, blank=True, null=True)
    phonenumber_location = models.FileField(
        upload_to="num_location/", null=True, blank=True
    )
    phonenumber_history = models.FileField(
        upload_to="num_history/", null=True, blank=True
    )
    damage = models.IntegerField(
        validators=[non_negative_validator], null=True, blank=True
    )
    stage_of_crime = models.BooleanField(null=True, blank=True)
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        unique_together = ("numEO", "date", "district")

    def __str__(self):
        return f"ЄО {self.numEO} від {self.date} ({self.district})"
