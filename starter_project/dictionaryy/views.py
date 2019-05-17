from django.shortcuts import render
from .models import Word

def home(request):
	context = {
		'words': Word.objects.all()
	}
	return render(request, 'dictionaryy/home.html', context)