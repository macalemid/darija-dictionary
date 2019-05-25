from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Word(models.Model):
	darija = models.CharField(max_length=100)
	arabic = models.CharField(max_length=100)
	english = models.CharField(max_length=100)
	explanation = models.TextField()
	picture = False
	audio = False
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.darija
	
	def get_absolute_url(self):
		return reverse('word-detail', kwargs={'pk': self.pk})