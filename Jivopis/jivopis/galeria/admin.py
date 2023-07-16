from django.contrib import admin
from .models import *


class SculpTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PaintTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PaintGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PaintingAdmin(admin.ModelAdmin):
    list_display = ('title', 'year',)
    search_fields = ('title', 'description', 'year',)


class SculptureAdmin(admin.ModelAdmin):
    list_display = ('title', 'year',)
    search_fields = ('title', 'description', 'year',)


admin.site.register(SculpType, SculpTypeAdmin)
admin.site.register(PaintType, PaintTypeAdmin)
admin.site.register(PaintGenre, PaintGenreAdmin)
admin.site.register(Authors, AuthorAdmin)
admin.site.register(Paintings, PaintingAdmin)
admin.site.register(Sculptures, SculptureAdmin)
