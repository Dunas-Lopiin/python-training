from rest_framework.views import APIView
from rest_framework.response import Response
from characters.models import Character
from django.forms.models import model_to_dict

class CharacterView(APIView):
    def post(self, request):
        
        character_data = request.data

        character = Character.objects.create(
            name = character_data["name"],
            specialization = character_data['specialization'],
            weapon = character_data['weapon'],
        )

        return Response(model_to_dict(character), 201)
    
    def get(self, request):
        characters = Character.objects.all()
        characters_dict = []
        for character in characters:
            c = model_to_dict(character)
            characters_dict.append(c)

        return Response(characters_dict)

class CharacterDetailView(APIView):
    def get(self, request, character_id):
        try:
            character = Character.objects.get(pk=character_id)
        
        except Character.DoesNotExist:
            return Response({'error': 'character not found'}, status.HTTP_404_NOT_FOUND)
        
        character_dict = model_to_dict(character)
        return Response(character_dict)
    
class CharacterFilterView(APIView):
    def get(self, request):
        char_name = request.query_params.get('name', None)

        characters = Character.objects.filter(name=char_name)

        characters_dict = [model_to_dict(character) for character in characters]
        return Response(characters_dict)
