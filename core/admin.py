from django.contrib import admin
from core.models import Icons

# Programa que efetua a coleta de ícones web em Python utilizando a biblioteca BeautifulSoup.

class IconsAdmin(admin.ModelAdmin):
    list_display = ('id', 'icons')

admin.site.register(Icons)