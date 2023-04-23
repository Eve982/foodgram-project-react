# Generated by Django 4.2 on 2023-04-23 16:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Название рецепта не может состоятьтолько из цифр и символов.', regex='^(?=.*[a-zA-Zа-яА-ЯёЁ])[\\p{Zs}\xa0]*$')], verbose_name='Название'),
        ),
    ]
