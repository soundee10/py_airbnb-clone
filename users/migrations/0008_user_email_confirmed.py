# Generated by Django 2.2.5 on 2021-11-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
