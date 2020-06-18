from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world! You're on the DnD homepage.")

def detail(request, character_id):
	return HttpResponse("You're looking at character %s." % character_id)

def party(request, party_id):
	party = "You're looking at party #%s."
	return HttpResponse(party % party_id)