from django import forms

from coreapp.utils import file_extension_validator


class ImportHealthUnityForm(forms.Form):
    file = forms.FileField(
        label='Arquivo', validators=(file_extension_validator,))