import json
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	if request.method == 'GET':
		return HttpResponse(
			"<html><body>" +
			"<p>Hello, World!</p>" +
			"<p>" + json.dumps(request.GET) + "</p>" +
			"</body></html>"
		)
	elif request.method == 'POST':
		return HttpResponse(
			"<html><body>" +
			"<p>Hello, World!</p>" +
			"<p>" + json.dumps(request.POST) + "</p>" +
			"</body></html>"
		)

def jsontest(request):
	return HttpResponse(json.dumps({
		'key1': 'value1',
		'key2': 'value2',
		'key3': 'value3',
	}))

def calendar(request):
	return render(request, 'calendar', context={})

def portal(request):
	return render(request, 'portal', context={})
