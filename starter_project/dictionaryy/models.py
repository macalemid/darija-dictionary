from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
	darija = models.CharField(max_length=100)
	arabic = models.CharField(max_length=100)
	english = models.CharField(max_length=100)
	explanation = models.TextField()
	picture = False
	audio = False
	author = models.ForeignKey(User, on_delete=models.CASCADE)
