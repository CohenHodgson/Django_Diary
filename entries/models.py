from django.db import models
from django.utils import timezone
# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length=200) # word limit?
	content = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural =  "Entries" # bc django will otherwise spell it as Entrys instead of Entries

