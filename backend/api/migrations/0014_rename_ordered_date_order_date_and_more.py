# Generated by Django 4.0.6 on 2022-10-24 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0013_alter_combo_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ordered_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_food',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('total', models.PositiveSmallIntegerField()),
                ('food', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='food',
            field=models.ManyToManyField(to='api.orderitem'),
        ),
    ]
