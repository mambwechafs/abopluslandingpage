from django.shortcuts import render

def home(request):
     context = {
        "basic_plan": {
            "name": "Basic",
            "price": 5.99,
            "features": [
                "Access to Now Showing Video on Demand",
                "Stream Movies and TV Shows",
                "Limited access to Original Content"
            ]
        },
        "standard_plan": {
            "name": "Standard",
            "price": 9.99,
            "features": [
                "Access to Now Showing Video on Demand",
                "Stream Movies and TV Shows",
                "Access to Original Content",
                "HD Video Quality"
            ]
        },
        "premium_plan": {
            "name": "Premium",
            "price": 14.99,
            "features": [
                "Access to Now Showing Video on Demand",
                "Stream Movies and TV Shows",
                "Full access to Original Content",
                "HD and Ultra HD Video Quality",
                "Downloadable content for offline viewing"
            ]
        }
    }
     return render(request, 'index.html', context)