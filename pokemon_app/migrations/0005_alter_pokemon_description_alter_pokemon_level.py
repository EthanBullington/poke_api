# Generated by Django 4.2.3 on 2023-07-12 14:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0004_pokemon_date_encountered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Unknown', validators=[django.core.validators.MinLengthValidator(25), django.core.validators.MaxLengthValidator(150)]),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
