from django.urls import path

from . import views

app_name = 'dndmain'
urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
	path('<int:pk>/party/', views.PartyView.as_view(), name = 'party'),
	path('character/<int:pk>/', views.CharacterView.as_view(), name = 'character')
]