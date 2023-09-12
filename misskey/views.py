import json
from django.http import HttpResponse
from .ms import note

def post(request):
	result = note(request.POST.get("text"))

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
