from django.urls import path

from urlshortener.views import ShortenerCreateView, redirect_url_view

urlpatterns = [
        path('', ShortenerCreateView.as_view(), name='home'),
        path('<str:shortened_part>', redirect_url_view, name='redirect'),
]

