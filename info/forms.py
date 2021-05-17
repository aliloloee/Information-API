from django import forms
from .models import Information


class InformationForm (forms.ModelForm) :
    slug = forms.SlugField(label='slug', max_length=250 , required=False, help_text='will be added automatically')

    class Meta :
        model = Information
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].widget.attrs.update(
            {'readonly':True})