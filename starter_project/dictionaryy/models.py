from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from simple_history.models import HistoricalRecords

class Dictionary(models.Model):
	darija = models.CharField(max_length=20, blank=True)
	arabic = models.CharField(max_length=20, blank=True)
	english = models.CharField(max_length=20, blank=True)
	history = HistoricalRecords()
	user = models.ForeignKey(
		User,
		null=True,
		on_delete=models.SET_NULL)
	def __str__(self):
		return str(self.darija)
	
	def get_absolute_url(self):
		return reverse('dictionary-detail', kwargs={'pk': self.pk})

