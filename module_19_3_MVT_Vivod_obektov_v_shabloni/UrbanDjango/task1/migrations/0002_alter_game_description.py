# Generated by Django 4.2.17 on 2025-01-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]