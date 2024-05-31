from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Waste Management Locations App!")
from django.shortcuts import render

# Create your views here.
# locations/views.py
from django.shortcuts import render
from .models import WasteDisposalLocation

def waste_disposal_location_list(request):
    locations = WasteDisposalLocation.objects.all()
    return render(request, 'locations/waste_disposal_location_list.html', {'locations': locations})
