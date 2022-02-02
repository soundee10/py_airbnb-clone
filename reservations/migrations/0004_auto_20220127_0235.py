# Generated by Django 2.2.5 on 2022-01-27 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_bookedday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=50),
        ),
    ]