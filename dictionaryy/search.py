from django.db.models import Q

def filter_words_based_on_search_input(searchWord, dictionaries):
  return dictionaries.filter( Q(darija__icontains=searchWord) | Q(arabic__icontains=searchWord) | Q(english__icontains=searchWord)).order_by('-id')