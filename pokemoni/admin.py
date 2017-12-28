from django.contrib import admin

from .models import Druzinka, Pokemon

@admin.register(Druzinka)
class DruzinkaAdmin(admin.ModelAdmin):
    fields = ('nazov',)

admin.site.register(Pokemon)
admin.site.register(Trener)
admin.site.register(Kurz)
admin.site.register(Ucet)
