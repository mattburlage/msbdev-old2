# Generated by Django 2.2.1 on 2019-05-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msbdev', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textcopy',
            name='classes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
