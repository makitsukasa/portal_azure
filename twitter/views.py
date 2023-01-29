import json
from django.http import HttpResponse
from .tw import update_status

def post(request):
	result = update_status(request.POST.get("text"))

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
