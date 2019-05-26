from django.shortcuts import render
from .models import Word
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	words = Word.objects.all()

	if('search' in request.GET):
		search_term = request.GET['search']
		words = Word.objects.filter(darija__contains=search_term)
	
	context = {
		'words': words
	}
	return render(request, 'dictionaryy/home.html', context)


class WordDetailView(DetailView):
	model = Word

class WordCreateView(LoginRequiredMixin, CreateView):
	model = Word
	fields = ['darija', 'arabic', 'english', 'explanation']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class WordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Word
	fields = ['darija', 'arabic', 'english', 'explanation']		

	def test_func(self):
		word = self.get_object()
		if self.request.user == word.author:
			return True
		return False