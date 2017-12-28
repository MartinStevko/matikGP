from django.urls import path

from . import views

app_name = 'pokemoni'

urlpatterns = [
    path('trening', views.TreningView.as_view(), name='trening'),
    path('trenuj', views.trenuj, name='trenuj')
]
