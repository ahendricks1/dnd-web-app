from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render

from .models import Party


# I recognize that this is very simple, I'm just getting my head around it!
def index(request):
	parties = Party.objects.order_by('-creation_date')[:5]
	context = { 'parties': parties }
	return render(request, 'dndmain/index.html', context)

def detail(request, party_id):
	party = get_object_or_404(Party, pk = party_id)
	return render(request, 'dndmain/detail.html', {'party': party})

def party(request, party_id):
	party = "You're looking at party #%s."
	return HttpResponse(party % party_id)