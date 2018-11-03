from django.shortcuts import render

# Create your views here.

def oferia_list(request):
    return render(request, "oferia/oferia_list.html", {})

