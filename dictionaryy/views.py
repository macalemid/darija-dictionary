from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Dictionary
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .search import filter_words_based_on_search_input
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
	
def about(request):
	return render(request, 'about.html', {'title': 'About'})

def dictionary(request):
	dictionaries = Dictionary.objects.all()
	if request.GET:
		if request.GET.get('english'):
			dictionaries =  dictionaries.order_by('english')
		elif request.GET.get('darija'):
			dictionaries = dictionaries.order_by('darija') 
		elif request.GET.get('arabic'):
			dictionaries = Dictionary.objects.order_by('arabic')
		elif request.GET.get('q'):
			dictionaries = filter_words_based_on_search_input(request.GET.get('q'), dictionaries)
	paginator = Paginator(dictionaries, 25)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'dictionaryy/dictionary.html', {'page_obj': page_obj})

def home(request):
	top_users = Profile.objects.all().order_by('-score')[:10]
	return render(request, 'dictionaryy/home.html', {'top_users': top_users})

class DictionaryListView(ListView):
	model = Dictionary
	template_name = 'dictionaryy/home.html'
	paginate_by = 3
	context_object_name = 'dicts'

class DictionaryCreateView(LoginRequiredMixin, CreateView):
	model = Dictionary
	fields = ['darija', 'arabic', 'english']
	def form_valid(self, form):
		auth = self.request.user
		form.instance.user = auth
		form.instance.author = auth
		form.save()
		Profile.objects.filter(user=auth).first().add1()
		return super().form_valid(form)

class DictionaryDetailView(DetailView):
	model = Dictionary

class DictionaryUpdateView(LoginRequiredMixin, UpdateView):
	model = Dictionary
	fields = ['darija', 'arabic', 'english']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class DictionaryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Dictionary
	success_url = '/'
	

	def delete(self, request, *args, **kwargs):
		Profile.objects.filter(user=self.request.user).first().sub1()
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)

	def test_func(self):
		return True

def contactView(request):
	return render(request, 'dictionaryy/contact.html')
