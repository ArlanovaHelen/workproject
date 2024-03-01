# Generated by Django 4.2.7 on 2024-02-17 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("frauds", "0011_bslocation_control_fraud_damage_fraud_stage_of_crime"),
    ]

    operations = [
        migrations.AddField(
            model_name="fraud",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
