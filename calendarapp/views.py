from django.shortcuts import render
from . import googlecalendar

def index(request):
	googlecalendar.get_events()
	return render(request, 'calendar.html', context={})
