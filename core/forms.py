from django import forms

from core import models


class BookSearch(forms.Form):
    title = forms.CharField(label='Поиск по названию', required=False)
    num_of_reviews = forms.IntegerField(label='и по кол-ву рецензий', min_value=0, required=False)

    def clean(self):
        name = self.cleaned_data['title']
        count = self.cleaned_data['num_of_reviews']
        if '/' or '!' in name:
            raise forms.ValidationError('Имя не должно содержать "/" или "!"')
        if count >> 30:
            raise forms.ValidationError('Число отзывов не должно превышать 30')
        return name


class BookForm(forms.ModelForm):
    title = forms.CharField(label="Название книги", required=False)
    summary = forms.CharField(widget=forms.Textarea, label="Краткое описание ", required=False)
    num_of_reviews = forms.IntegerField(label="Кол-во рецензий критиков", required=False)

    class Meta:
        model = models.Book
        fields = "__all__"
