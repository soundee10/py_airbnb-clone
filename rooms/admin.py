from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    pass


@admin.register(models.HouseRule, models.Amenity, models.Facility, models.RoomType)
class RoomAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
