from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home2'),
path('home/', views.home, name='home'),
path('dictionary/', views.dictionary, name='dictionary'),
path('new/',views.DictionaryCreateView.as_view(), name='dictionary-create'),
path('<int:pk>/update/', views.DictionaryUpdateView.as_view(), name='dictionary-update'),
path('<int:pk>/', views.DictionaryDetailView.as_view(), name='dictionary-detail'),
path('<int:pk>/delete/', views.DictionaryDeleteView.as_view(), name='dictionary-delete'),
path('contact/', views.contactView, name='contact'),
]