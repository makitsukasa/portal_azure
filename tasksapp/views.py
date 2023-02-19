import json
from django.http import HttpResponse
from django.shortcuts import render
from . import googletasks

def index(request):
	return render(request, "tasks.html", context={"tasks": googletasks.list_tasks()})

def insert(request):
	result = googletasks.insert_task(request.POST.get("text"))

	if result:
		return HttpResponse(json.dumps({
			"result": "true",
		}))
	else:
		return HttpResponse(json.dumps({
			"result": "false",
		}))

def get(request):
	return HttpResponse(vars(request))
