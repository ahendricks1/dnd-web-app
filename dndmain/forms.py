from django import forms
from django.contrib.auth.models import User

from .models import Character

class CharacterForm(forms.ModelForm):
	class Meta:
		model = Character
		fields = [
			'char_name',
			'health',
			'armor_class',
			'speed',
			'init',
			'strength',
			'dex',
			'constitution',
			'intelligence',
			'wisdom',
			'charisma'
		]