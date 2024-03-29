# Generated by Django 4.1.5 on 2024-02-27 07:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_offers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offers',
            options={'verbose_name_plural': 'Offers'},
        ),
        migrations.AddField(
            model_name='offers',
            name='offer_date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='offer_ends',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='offer_starts',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
