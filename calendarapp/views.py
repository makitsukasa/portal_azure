import json
from django.shortcuts import render
from django.http import HttpResponse
from . import googlecalendar

def index(request):
	return render(request, 'calendar.html', context=googlecalendar.get_events())

def hidden(request):
	return render(request, 'calendar.html', context=googlecalendar.get_events(show_hidden=True))

def create(request):
	result = googlecalendar.create_event(
		request.POST.get("text"), request.POST.get("date"), request.POST.get("color"))

	if result:
		return HttpResponse(json.dumps({
			"result": "true",
		}))
	else:
		return HttpResponse(json.dumps({
			"result": "false",
		}))

def update(request):
	result = googlecalendar.update_event(
		request.POST.get("id"), request.POST.get("text"),
		request.POST.get("date"), request.POST.get("color"))

	if result:
		return HttpResponse(json.dumps({
			"result": "true",
		}))
	else:
		return HttpResponse(json.dumps({
			"result": "false",
		}))

def delete(request):
	result = googlecalendar.delete_event(request.POST.get("id"))

	if result:
		return HttpResponse(json.dumps({
			"result": "true",
		}))
	else:
		return HttpResponse(json.dumps({
			"result": "false",
		}))
