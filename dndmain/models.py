from django.db import models

class Party(models.Model):
	dungeon_master = models.CharField(max_length = 100)
	creation_date = models.DateTimeField('date published')

	def __str__(self):
		return self.dungeon_master

	def was_created_recently(self):
		return self.creation_date >= timezone.now() - datetime.timedelta(days = 1)

class Character(models.Model):
	party = models.ForeignKey(Party, on_delete = models.CASCADE)
	real_name = models.CharField(max_length = 100)
	char_name = models.CharField(max_length = 100)

	def __str__(self):
		return self.char_name
