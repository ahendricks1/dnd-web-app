from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Party, Character
from .forms import CharacterForm

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

@login_required
def profile(request, user_id):
	user = get_object_or_404(User, pk = user_id)
	characters = Character.objects.all().filter(user = user)
	return render(request, 'dndmain/profile.html', {'characters': characters})

def create(request):
	if not request.user.is_authenticated:
		return render(request, 'dndmain/home.html')

	else:
		form = CharacterForm(request.POST or None)
		if(form.is_valid()):
			user = form.save()
			context = {
				'form': form
			}

		return render(request, 'dndmain/create.html', context)