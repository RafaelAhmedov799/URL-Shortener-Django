from django import forms
from urlshortener.models import URL

# форма на основе модели
class ShortenerForm(forms.ModelForm):
    # поле для ввода длинной ссылки
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "url-input", "placeholder": "Your URL to shorten"}))

    class Meta:
        # модель, на которой строится форма
        model = URL
        # поля, которые будут показаны пользователю
        fields = ('long_url',) # только поле для ввода длинной ссылки

