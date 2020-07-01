from django.db import models
from django.contrib.auth.models import User

class Party(models.Model):
	dungeon_master = models.CharField(max_length = 100)
	creation_date = models.DateTimeField('date published')

	def __str__(self):
		return self.dungeon_master

	def was_created_recently(self):
		return self.creation_date >= timezone.now() - datetime.timedelta(days = 1)

class Character(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	party = models.ForeignKey(Party, on_delete = models.CASCADE)
	real_name = models.CharField(max_length = 100)
	char_name = models.CharField(max_length = 100)
	health = models.IntegerField(default = 0)
	current_hp = models.IntegerField(default = 0)
	armor_class = models.IntegerField(default = 0)
	speed = models.IntegerField(default = 0)
	init = models.IntegerField(default = 0)
	strength = models.IntegerField(default = 10)
	dex = models.IntegerField(default = 0)
	constitution = models.IntegerField(default = 0)
	intelligence = models.IntegerField(default = 0)
	wisdom = models.IntegerField(default = 0)
	charisma = models.IntegerField(default = 0)

	def __str__(self):
		return self.char_name
