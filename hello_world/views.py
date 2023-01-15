import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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

