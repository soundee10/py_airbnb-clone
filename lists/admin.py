from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    """List Admin Registration"""

    list_display = (
        "name",
        "users",
        "count_rooms",
    )
    filter_horizontal = ("rooms",)
    search_fields = ("name",)
