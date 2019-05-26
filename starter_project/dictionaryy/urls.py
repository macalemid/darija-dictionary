from django.urls import path
from . import views



urlpatterns = [
path('', views.home, name='dictionary'),
path('word/<int:pk>/', views.WordDetailView.as_view(), name='word-detail'),
path('word/new/', views.WordCreateView.as_view(), name='word-create'),
path('word/<int:pk>/update', views.WordUpdateView.as_view(), name='word-update'),

    ]