# Generated by Django 4.1.5 on 2023-02-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=20)),
                ('card_type', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('value', models.IntegerField()),
            ],
        ),
    ]
