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

class WordD(models.Model):
	LANGUAGES = [
		('D', 'Darija'),
		('A', 'Arabic'),
		('E', 'English'),
		]
	Language = models.CharField(max_length=1, choices=LANGUAGES)
	plural = models.CharField(max_length=20)
	root = models.CharField(max_length=10)
	audio = models.FileField(upload_to='audio/')

class Dictionary(models.Model):
	words = models.ManyToManyField(WordD)
	explanation = models.CharField(max_length=10000)
	picture = models.ImageField(upload_to='images/')
	tags = []

	