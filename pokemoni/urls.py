from django.urls import path

from . import views

app_name = 'pokemoni'

urlpatterns = [
    path('trening', views.trening, name='trening'),
    path('obchod', views.obchod, name='obchod'),
    path('prehlad', views.prehlad, name='prehlad'),
    path('druzinka/<int:num>', views.druzinka, name='druzinka')
]
