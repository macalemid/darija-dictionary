from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='dictionary'),
path('word/new/',views.make_word, name='new-word'),
path('word/<int:pk>/', views.WordDetailView.as_view(), name='word-detail'),

    ]