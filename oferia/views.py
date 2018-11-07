from django.shortcuts import render, get_object_or_404
from .models import Offer

# Create your views here.

def oferia_list(request):
    displayAll = Offer.objects.all()
    return render(request, "oferia/oferia_list.html", {'allOffers': displayAll})

def offer_detail(request, pk):
    offer = get_object_or_404(Offer, pk = pk)
    return render(request, "oferia/offer_detail.html", {'detailedOffer': offer})
