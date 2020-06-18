from django.db import models

class Party(models.Model):
	dungeon_master = models.CharField(max_length = 100)
	creation_date = models.DateTimeField('date published')

class Character(models.Model):
	party = models.ForeignKey(Party, on_delete = models.CASCADE)
	real_name = models.CharField(max_length = 100)
	char_name = models.CharField(max_length = 100)	
