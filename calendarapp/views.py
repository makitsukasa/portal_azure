import json
from django.shortcuts import render
from django.http import HttpResponse
from . import googlecalendar

def index(request):
	return render(request, 'calendar.html', context=googlecalendar.get_events())

def hidden(request):
	return render(request, 'calendar.html', context=googlecalendar.get_events(show_hidden=True))

def insert(request):
	result = googlecalendar.insert_event(
		request.POST.get("text"), request.POST.get("date"), request.POST.get("color"))

	if result:
		return HttpResponse(json.dumps({
			"result": "true",
		}))
	else:
		return HttpResponse(json.dumps({
			"result": "false",
		}))
