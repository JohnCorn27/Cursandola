from django.contrib import admin
from .models import Page, Categoria, Video

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)

admin.site.register(Categoria, PageAdmin)

admin.site.register(Video, PageAdmin)