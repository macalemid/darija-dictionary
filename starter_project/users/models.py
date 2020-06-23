from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) # change this later
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	score = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.user.username} Profile'

	def add1(self):
		self.score += 1
		self.save()

	def sub1(self):
		self.score -= 1
		self.save()