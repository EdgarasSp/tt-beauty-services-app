# Generated by Django 3.2 on 2022-06-30 16:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20220630_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-received_date']},
        ),
        migrations.AddField(
            model_name='booking',
            name='received_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Contacted')], default=0),
        ),
    ]