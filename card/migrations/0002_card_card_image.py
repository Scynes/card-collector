# Generated by Django 4.1.5 on 2023-02-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_image',
            field=models.CharField(default='none', max_length=255),
        ),
    ]
