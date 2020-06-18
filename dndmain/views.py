from django.http import HttpResponse
from django.template import loader

from .models import Party


# I recognize that this is very simple, I'm just getting my head around it!
def index(request):
	parties = Party.objects.order_by('-creation_date')[:5]
	template = loader.get_template('dndmain/index.html')
	context = {
		'parties': parties,
	}
	return HttpResponse(template.render(context, request))

def detail(request, character_id):
	return HttpResponse("You're looking at character %s." % character_id)

def party(request, party_id):
	party = "You're looking at party #%s."
	return HttpResponse(party % party_id)