from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world! You're on the DnD homepage.")