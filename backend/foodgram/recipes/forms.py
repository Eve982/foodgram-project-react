from django.forms import ModelForm

from .models import IngredientImport


class IngredientImportForm(ModelForm):
    class Meta:
        model = IngredientImport
        fields = ('csv_file',)
