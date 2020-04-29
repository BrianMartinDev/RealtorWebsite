from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing


# /listings
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


# /listings/1
def listing(request, listing_id):
    listings_id = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listings_id
    }
    return render(request, 'listings/listing.html', context)


# /listings/search?keywords=&city=
def search(request):
    return render(request, 'listings')
