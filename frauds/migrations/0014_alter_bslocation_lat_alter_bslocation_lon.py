# Generated by Django 5.0.2 on 2024-02-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frauds', '0013_phonenumberfile_user_alter_phonenumberfile_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bslocation',
            name='lat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bslocation',
            name='lon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
