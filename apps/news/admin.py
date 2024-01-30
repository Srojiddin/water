from django.contrib import admin

from apps.news.models import News


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['description']

