from django.contrib import admin

import rooms
from . import models

# Register your models here.


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    list_display = (
        "room",
        "in_progress",
        "guest",
        "check_in",
        "check_out",
        "is_finished",
    )

    list_filter = ("status",)
    # list_filter = ("status", "in_progress")
