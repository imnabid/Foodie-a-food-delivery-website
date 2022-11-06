# Generated by Django 4.0.6 on 2022-11-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_carouselimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_hrs', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('delivery_charge', models.PositiveSmallIntegerField(default=0)),
                ('fb', models.CharField(max_length=200)),
                ('insta', models.CharField(max_length=200)),
            ],
        ),
    ]