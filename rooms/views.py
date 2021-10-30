from django.shortcuts import render, redirect
from django_countries import countries
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from . import models

# from django.core.paginator import EmptyPage, Paginator
# from django.urls import reverse


class HomeView(ListView):
    """Home View Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    ordering = "created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404
        # return redirect(reverse("core:home"))


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_types", 0))
    price = request.GET.get("price", 0)
    guests = request.GET.get("guests", 0)
    bedrooms = request.GET.get("bedrooms", 0)
    beds = request.GET.get("beds", 0)
    baths = request.GET.get("baths", 0)
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    # form = everything we get from the request
    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "superhost": superhost,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}
    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if guests != 0:
        filter_args["guests__gte"] = guests

    if price != 0:
        filter_args["price__gte"] = price

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True

    rooms = models.Room.objects.filter(**filter_args)

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            rooms = rooms.filter(amenities__pk=int(s_amenity))
            # filter_args["amenities__pk"] = int(s_amenities)

    if len(s_facilities) > 0:
        for s_amenity in s_facilities:
            rooms = rooms.filter(facilities__pk=int(s_amenity))
            # filter_args["facilities__pk"] = int(s_facilities)
    return render(
        request,
        "rooms/search.html",
        {**form, **choices, "rooms": rooms},
    )


""" 
# using pagination in manual...
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, 3)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", context={"page": rooms})
    except EmptyPage:
        return redirect("/")
"""

""" pagination in manual"""
"""
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    page_count = ceil(models.Room.objects.count() / page_size)
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
"""
