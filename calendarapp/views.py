from django.shortcuts import render
from . import googlecalendar

def index(request):
	return render(request, 'calendar.html', context=googlecalendar.get_events())
