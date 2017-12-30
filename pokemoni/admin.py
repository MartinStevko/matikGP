from django.contrib import admin

from .models import Druzinka, Pokemon, Trener, Kurz, Ucet

@admin.register(Druzinka)
class DruzinkaAdmin(admin.ModelAdmin):
    fields = ('nazov','url_number',)

admin.site.register(Pokemon)
admin.site.register(Trener)
admin.site.register(Kurz)
admin.site.register(Ucet)
