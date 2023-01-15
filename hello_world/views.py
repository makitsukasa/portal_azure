from django.http import HttpResponse

def index(request):
	return HttpResponse("<html><body>IHello world</body></html>")
