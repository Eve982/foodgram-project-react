# Generated by Django 4.2 on 2023-04-22 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_ingredientimport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IngredientImport',
        ),
    ]