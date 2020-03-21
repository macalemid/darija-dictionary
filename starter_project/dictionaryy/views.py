from django.shortcuts import render, redirect
from .models import Dictionary, WordD
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WordForm
from django.urls import reverse
from django.views.generic import DetailView
	

from dictionaryy.models import Dictionary, WordD
def home(request):
	dicts = Dictionary.objects.all()
	"""
	if('search' in request.GET):
		search_term = request.GET['search']
		words = Word.objects.filter(darija__contains=search_term)
	"""
	context = {
		'dicts': dicts
	}
	return render(request, 'dictionaryy/home.html', context)

def make_word(request):
	if request.method == 'POST':
		form = WordForm(request.POST)
		if form.is_valid():
			darija = WordD(language='D', word= form.cleaned_data['darija'])
			arabic = WordD(language='A', word= form.cleaned_data['arabic'])
			english = WordD(language='E', word= form.cleaned_data['english'])
			diction = Dictionary(explanation=form.cleaned_data['explanation'])
			
			
			darija.save()
			arabic.save()
			english.save()
			diction.save()


			diction.words.add(darija, arabic, english)
			#add user to diction here
			return redirect('dictionary')
			#return reverse('word-detail', kwargs={'pk': diction.pk})
	else:
		form = WordForm()
	return render(request, 'dictionaryy/dictionary_form.html', {'form': form})

class WordDetailView(DetailView):
	model = Dictionary
