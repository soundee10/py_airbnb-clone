# Generated by Django 2.2.5 on 2021-11-02 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20211018_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='how many guests are coming with you?'),
        ),
    ]