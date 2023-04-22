# Generated by Django 4.2 on 2023-04-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_ingredient_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]