from django.urls import path

from . import views

app_name = 'pokemoni'

urlpatterns = [
    path('trening', views.trening, name='trening')
]
