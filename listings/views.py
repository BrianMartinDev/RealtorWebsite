from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Listing


def index(request):
    listings = Listing.objects.all()

    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request):
    return render(request, 'listings/listings.html')


def search(request):
    return render(request, 'listings')