from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "this command creates facilities"

    #    def add_arguments(self, parser):
    #       parser.add_argument("--times", help="how many times do you want?")

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        # room_models.Amenity.objects.create()
        for f in facilities:
            room_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))
