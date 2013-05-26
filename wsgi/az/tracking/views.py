# Create your views here.
from django.http import HttpResponse
from tracking.models import Tracking
from django.shortcuts import render, get_object_or_404

from django.utils.translation import ugettext as _

def index(request):
	output = _("Welcome to my site.")
	return HttpResponse(output)

def details(request, tracking_number):
	tracking = get_object_or_404(Tracking, tracking_number=tracking_number)
	return render(request, 'tracking/details.html', {'tracking': tracking})