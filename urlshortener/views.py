from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views.generic.edit import CreateView

from urlshortener.models import URL
from urlshortener.forms import ShortenerForm

# Create your views here.
# Представление для создания нового объекта
class ShortenerCreateView(CreateView):
    model = URL
    form_class = ShortenerForm

    #
    def form_valid(self, form):
        shortener = form.save(commit=False) # считывание формы
        shortener.create_short_url() # генерация короткой ссылки 
        shortener.save() # сохранение в таблицу базы данных

        # сбор данных для шаблона
        long_url = shortener.long_url
        new_url = self.request.build_absolute_uri('/') + shortener.short_url
        context = {
                "new_url": new_url,
                "long_url": long_url,
                "form": ShortenerForm(),
                }

        return render(self.request, 'urlshortener/url_form.html', context)

# перенаправление при переходе по короткой ссылке на длинную ссылку
def redirect_url_view(request, shortened_part):
    try:
        url = URL.objects.get(short_url=shortened_part)# получаем объект из таблицы, ищем по короткой ссылке
        url.times_followed += 1    # увеличиваем счетчик переходов по ссылке
        url.save() # сохраняем объект в базу данных, чтобы счетчик обновился
        
        return HttpResponseRedirect(url.long_url) # перенаправляем по длинной ссылке
        
    except:
        raise Http404('Sorry this link is broken :(') # если не нашли короткую ссылку, то выводим сообщение, что ссылка битая
