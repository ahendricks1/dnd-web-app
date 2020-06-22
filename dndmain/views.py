from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Party, Character


class IndexView(generic.ListView):
	template_name = 'dndmain/index.html'
	context_object_name = 'parties'

	def get_queryset(self):
		return Party.objects.order_by('-creation_date')[:5]

class DetailView(generic.DetailView):
	model = Party
	template_name = 'dndmain/detail.html'

class CharacterView(generic.DetailView):
	model = Character
	template_name = 'dndmain/character.html'

class PartyView(generic.DetailView):
	model = Party
	template_name = 'dndmain/detail.html'

# I recognize that this is very simple, I'm just getting my head around it!
#def (request):
#	parties = Party.objects.order_by('-creation_date')[:5]
#	context = { 'parties': parties }
#	return render(request, 'dndmain/index.html', context)
#
#def detail(request, party_id):
#	party = get_object_or_404(Party, pk = party_id)
#	return render(request, 'dndmain/detail.html', {'party': party})
#
#def character(request, character_id):
#	character = get_object_or_404(Character, pk = character_id)
#	return render(request, 'dndmain/character.html', {'character': character})
#
#def party(request, party_id):
#	party = "You're looking at party #%s."
#	return HttpResponse(party % party_id)