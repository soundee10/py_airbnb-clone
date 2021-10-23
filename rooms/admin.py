from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More about Spaces",
            {
                # "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rule"),
            },
        ),
        (
            "Last Details",
            {
                "fields": ("host",),
            },
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photo",
        "total_rating",
    )

    # ordering = ('name')

    list_filter = (
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
    )

    raw_id_fields = ("host",)

    inlines = (PhotoInline,)

    search_fields = ("city",)
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photo(self, obj):
        return obj.photos.count()

    count_photo.short_description = "PHOTO COUNT"


@admin.register(models.HouseRule, models.Amenity, models.Facility, models.RoomType)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="70px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
