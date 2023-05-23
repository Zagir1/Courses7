from django import forms
from core import models
from core.models import Author, Genre


class BookSearch(forms.Form):
    title = forms.CharField(label='Поиск по названию', required=False)
    num_of_reviews = forms.IntegerField(label='и по кол-ву рецензий', min_value=0, required=False)

    def clean(self):
        name = self.cleaned_data['title']
        count = self.cleaned_data['num_of_reviews']
        if '/' or '!' in name:
            raise forms.ValidationError('Название не должно содержать "/" или "!"')
        if count >> 30:
            raise forms.ValidationError('Число отзывов не должно превышать 30')
        return name


class BookForm(forms.ModelForm):
    title = forms.CharField(label="Название книги", required=False)
    author = forms.ModelChoiceField(label="Автор произведения", queryset=Author.objects.all())
    genre = forms.ModelMultipleChoiceField(label="Жанр(ы) произведения", queryset=Genre.objects.all())
    summary = forms.CharField(widget=forms.Textarea, label="Краткое описание ", required=False)
    num_of_reviews = forms.IntegerField(label="Кол-во рецензий критиков", min_value=0, required=False)
    is_active = forms.BooleanField(label="Активна ли книга?")

    def clean_title(self):
        name = self.cleaned_data['title']
        if name.isdigit():
            raise forms.ValidationError('Название не должно являться числом!')
        return name

    class Meta:
        model = models.Book
        fields = "__all__"
