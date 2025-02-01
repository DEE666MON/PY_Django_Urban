from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(Game)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "cost", "size")
    list_filter = ("size", "cost")
    search_fields = ("title",)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "age")
    list_filter = ("balance", "age")
    search_fields = ("name",)
    list_per_page = 30


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "date")
    list_filter = ("date",)
    search_fields = ("title", "content")
    list_per_page = 2
