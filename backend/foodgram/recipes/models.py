from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField('Название',
                            max_length=settings.LENGHT_MAX)
    measurement_unit = models.CharField('Единица измерения',
                                        max_length=settings.LENGHT_MAX)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name', ]

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class IngredientImport(models.Model):
    csv_file = models.FileField(upload_to='uploads/')
    date_added = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField('Название', unique=True,
                            max_length=settings.LENGHT_MAX)
    color = models.CharField(
        'Цветовой HEX-код',
        unique=True,
        max_length=settings.LENGHT_COLOR,
        validators=[
            RegexValidator(
                regex=settings.COLOR_REGEX,
                message='Введенное значение не является цветом в формате HEX.'
            )
        ]
    )
    slug = models.SlugField('Уникальный слаг', unique=True,
                            max_length=settings.LENGHT_MAX)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField('Название', max_length=settings.LENGHT_MAX)
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
    )
    text = models.TextField('Описание')
    image = models.ImageField(
        'Фотография',
        upload_to='recipes/'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[MinValueValidator(
            settings.COOKING_TIME_MIN_VALUE,
            message='Время приготовления не может быть равно нулю.'),
            MaxValueValidator(
            settings.COOKING_TIME_MAX_VALUE,
            message='Время приготовления не может превышать'
            'максимальное значение.'
        )]
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги'
    )

    class Meta:
        ordering = ['-id', ]
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
        validators=[MinValueValidator(
            settings.INGREDIENT_MIN_AMOUNT,
            message='Это значение не должно быть равно нулю.'),
            MaxValueValidator(
            settings.COOKING_TIME_MAX_VALUE,
            message='Время приготовления не может превышать'
            'максимальное значение.'
        )]
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'

    def __str__(self):
        return (
            f'{self.ingredient.name} ({self.ingredient.measurement_unit})'
            f' - {self.amount} '
        )


class UserRecipeAbstractBaseModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )

    class Meta:
        abstract = True


class Favourite(UserRecipeAbstractBaseModel):

    class Meta:
        default_related_name = 'favorites'
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            UniqueConstraint(fields=['user', 'recipe', ],
                             name='unique_favourite')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(UserRecipeAbstractBaseModel):

    class Meta:
        default_related_name = 'shopping_cart'
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзина покупок'
        constraints = [
            UniqueConstraint(fields=['user', 'recipe', ],
                             name='unique_shopping_cart')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Корзину покупок'
