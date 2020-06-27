from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Party, Character

def home(request):
	parties = Party.objects.order_by('-creation_date')[:5]
	context = { 'parties': parties }
	return render(request, 'dndmain/home.html', context)

def campaign(request):
	characters = Character.objects.all()
	return render(request, 'dndmain/campaign.html', {'characters': characters})

def character(request, character_id):
	character = get_object_or_404(Character, pk = character_id)
	return render(request, 'dndmain/character.html', {'character': character})

def party(request, party_id):
	party = "You're looking at party #%s."
	return HttpResponse(party % party_id)
