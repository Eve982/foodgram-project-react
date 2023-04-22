import csv

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка данных из csv файлов'

    def add_arguments(self, parser):
        parser.add_argument(
            'ingredients_file',
            type=str,
            help='Путь к .csv файлу с ингридиентами.')

    def handle(self, *args, **kwargs):
        with open(
            kwargs.get('ingredients_file'),
            'r',
            encoding='utf-8'
        ) as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=['name',
                                                          'measurement_unit'])

            try:
                ingredient_objs = [Ingredient(**item)
                                   for item in reader]

                Ingredient.objects.bulk_create(ingredient_objs)

            except IntegrityError:
                return 'Такие ингредиенты уже есть...'
        return (
            f'{Ingredient.objects.count()} - ингредиентов успешно загружено')
