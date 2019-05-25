
from . import views
from django.urls import path


urlpatterns = [
path('', views.home, name='dictionary'),
path('word/<int:pk>/', views.WordDetailView.as_view(), name='word-detail'),
path('word/new/', views.WordCreateView.as_view(), name='word-create'),
    ]