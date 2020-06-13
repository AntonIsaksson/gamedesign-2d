# Generated by Django 2.1.5 on 2020-06-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0025_auto_20200613_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designs',
            name='character_type',
        ),
        migrations.AddField(
            model_name='designs',
            name='landscape_type',
            field=models.CharField(choices=[('forest', 'Forest'), ('dessert', 'Dessert'), ('city', 'City'), ('mountains', 'Mountains'), ('other', 'Other')], default='Neutral', max_length=30),
        ),
    ]