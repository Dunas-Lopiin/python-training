from django.urls import path
from .views import CharacterView, CharacterDetailView, CharacterFilterView

urlpatterns = [
    path('characters/', CharacterView.as_view()),
    path('characters/charname/', CharacterFilterView.as_view()),
    path('characters/<int:character_id>/', CharacterDetailView.as_view()),
]
