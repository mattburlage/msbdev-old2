# Generated by Django 2.2.1 on 2019-05-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextCopy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Internal Name')),
                ('html', models.TextField(verbose_name='HTML')),
            ],
        ),
    ]