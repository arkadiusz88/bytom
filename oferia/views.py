from django.shortcuts import render
from .models import Offer

# Create your views here.

def oferia_list(request):
    displayAll = Offer.objects.all()
    return render(request, "oferia/oferia_list.html", {'allOffers': displayAll})

