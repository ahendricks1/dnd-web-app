from django.urls import path

from . import views

app_name = 'dndmain'

urlpatterns = [
	path('', views.home, name = 'home'),
	path('campaign/', views.campaign, name = 'campaign'),
	path('party/<int:pk>/', views.party, name = 'party'),
	path('character/<int:character_id>/', views.character, name = 'character'),
	path('accounts/profile', views.profile, name = 'profile')
]
