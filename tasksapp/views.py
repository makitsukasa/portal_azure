import json
from django.http import HttpResponse
from . import googletasks


def insert(request):
	result = googletasks.insert_task(request.POST.get("text"))

	if result:
		return HttpResponse(json.dumps({
			'result': 'true',
		}))
	else:
		return HttpResponse(json.dumps({
			'result': 'false',
		}))

def get(request):
	return HttpResponse(vars(request))
