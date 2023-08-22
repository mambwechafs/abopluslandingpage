from django.shortcuts import render
from .models import GalleryItem

def home(request):
    gallery_items = GalleryItem.objects.all()
    context = {
        "subscription_name": "ABO PLUS",
        "zambia_price": "K110",
        "world_price": "$5.99",
        "features": [
            "Access to PLUS ORIGINALS",
            "Access to NOW SHOWING Movies and TV Shows",
            "Buy movies and premium series from BoxOffice"
        ],
        'gallery_items': gallery_items
    }
    return render(request, 'index.html', context)