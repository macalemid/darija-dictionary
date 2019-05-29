from django.shortcuts import render
from .models import Word
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

