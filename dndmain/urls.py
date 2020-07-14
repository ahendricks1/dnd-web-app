from django.urls import path

from . import views

app_name = 'dndmain'

urlpatterns = [
	path('', views.home, name = 'home'),
	path('campaign/', views.campaign, name = 'campaign'),
	path('party/<int:pk>/', views.party, name = 'party'),
	path('character/<int:character_id>/', views.character, name = 'character'),
	path('character/<int:character_id>/edit/', views.edit_character, name = 'edit_character'),
	path('character/<int:character_id>/delete/', views.delete_character, name = 'delete_character'),
	path('profile/<int:user_id>/', views.profile, name = 'profile'),
	path('create/<int:user_id>/', views.create, name = 'create'),
]
