# Generated by Django 4.0.6 on 2022-11-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_carouselimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
