from django.db import models


class PhonenumberFile(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    data = models.FileField(upload_to="num_history/")
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name
