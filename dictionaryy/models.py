from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse

class Dictionary(models.Model):
	darija = models.CharField(
		max_length=20,
		blank=True,
		validators = [
			RegexValidator('^[\u0621-\u064A\u0660-\u0669a-zA-Z0-9 ]+$', "Darija can only contain Latin/Arabic letters and numerals.", code="darija-invalid")
    ]
  )
	arabic = models.CharField(
		max_length=20,
		blank=True,
		validators = [
		  RegexValidator('^[\u0621-\u064A\u0660-\u0669 ]+$', "Arabic can only contain Arabic letters and numerals.", code="arabic-invalid")
    ]
  )
	english = models.CharField(
		max_length=20,
		blank=True,
		validators = [
			RegexValidator('^[a-zA-Z0-9 ]+$', "English can only contain Latin letters and numerals.", code="darija-invalid")
      ]
		)
	user = models.ForeignKey(
		User,
		null=True,
		on_delete=models.SET_NULL)
	def __str__(self):
		return str(self.darija)
	
	def get_absolute_url(self):
		return reverse('dictionary-detail', kwargs={'pk': self.pk})