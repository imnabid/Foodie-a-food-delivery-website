# Generated by Django 4.0.6 on 2022-10-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_comboitem_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
