# Generated by Django 3.2 on 2022-06-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20220627_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='status',
            field=models.IntegerField(choices=[(0, 'Repoly'), (1, 'Completed')], default=0),
        ),
    ]
