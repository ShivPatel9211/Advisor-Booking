# Generated by Django 3.2.8 on 2021-10-24 03:36

import User.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20211024_0907'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', User.manager.UserManager()),
            ],
        ),
    ]
