# Generated by Django 3.2.8 on 2021-10-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
