# Generated by Django 4.0.6 on 2022-08-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_verified_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.EmailField(blank=True, max_length=150, null=True, verbose_name='address'),
        ),
    ]