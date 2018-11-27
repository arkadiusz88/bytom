from django.shortcuts import render, get_object_or_404
from .models import Offer
from .forms import OfferForm
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.

def oferia_list(request):
    displayAll = Offer.objects.all()
    return render(request, "oferia/oferia_list.html", {'allOffers': displayAll})

def offer_detail(request, pk):
    offer = get_object_or_404(Offer, pk = pk)
    return render(request, "oferia/offer_detail.html", {'detailedOffer': offer})


def offer_new(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit = False)
            offer.author = request.user
            offer.published_date = timezone.now()
            offer.save()
            return redirect('offer_detail', pk = offer.pk)
    else:
        form = OfferForm
    return render(request, "oferia/offer_edit.html", {'form' : form})


def offer_edit(request, pk):
    offer = get_object_or_404(Offer, pk = pk)

    if request.method == 'POST':
        form = OfferForm(request.POST, instance=offer)
        if form.is_valid():
            offer = form.save(commit = False)
            offer.author = request.user
            offer.published_date = timezone.now()
            offer.save()
            return redirect('offer_detail', pk = offer.pk)
    else:
        form = OfferForm(instance=offer)
    return render(request, "oferia/offer_edit.html", {'form' : form})


def job_list(request):
    return render(request, "oferia/job_search.html")

def sign_up(request):
    return render(request, "oferia/sign_up.html")

