# Generated by Django 2.2.5 on 2021-11-02 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0003_auto_20211102_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='users',
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list', to=settings.AUTH_USER_MODEL),
        ),
    ]
