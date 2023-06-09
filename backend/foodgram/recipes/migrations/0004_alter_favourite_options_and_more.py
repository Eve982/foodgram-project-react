# Generated by Django 4.2 on 2023-04-21 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_favourite_options_alter_shoppingcart_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favourite',
            options={'default_related_name': 'favorites', 'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Это значение не должно быть равно нулю.'), django.core.validators.MaxValueValidator(4320, message='Время приготовления не может превышатьмаксимальное значение.')], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Время приготовления не может быть равно нулю.'), django.core.validators.MaxValueValidator(4320, message='Время приготовления не может превышатьмаксимальное значение.')], verbose_name='Время приготовления'),
        ),
    ]
