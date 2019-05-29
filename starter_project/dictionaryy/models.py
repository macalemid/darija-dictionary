from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Word(models.Model):
	pass

class WordD(models.Model):
	LANGUAGES = [
		('D', 'Darija'),
		('A', 'Arabic'),
		('E', 'English'),
		]
	word = models.CharField(max_length=201, null=True)
	language = models.CharField(max_length=1, choices=LANGUAGES)
	plural = models.CharField(max_length=20)
	root = models.CharField(max_length=10)
	audio = models.FileField(upload_to='audio/')

	def __str__(self):
		return self.word

class Dictionary(models.Model):
	words = models.ManyToManyField(WordD)
	explanation = models.CharField(max_length=10000)
	picture = models.ImageField(upload_to='images/')
	tags = []
	user = models.ForeignKey(
		User,
		null=True,
		on_delete=models.SET_NULL
		)

	def get_darija(self):
		return self.words.filter(language='D').first()

	def get_arabic(self):
		return self.words.filter(language='A').first()

	def get_english(self):
		return self.words.filter(language='E').first()

	def __str__(self):
		return self.explanation
	
	def get_absolute_url(self):
		return reverse('word-detail', kwargs={'pk': self.pk})

	