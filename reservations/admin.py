from django.contrib import admin

import rooms
from . import models

# Register your models here.


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    list_display = (
        "room",
        "status",
        "guest",
        "check_in",
        "check_out",
        "is_finished",
        "in_progress",
    )

    list_filter = ("status",)
    # list_filter = ("status", "in_progress")
