from django.shortcuts import render
from .models import Pokemon
from move_app.models import Move
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
import json
# Create your views here.
class All_Pokemon(APIView):

    def get(self, request):
        # Select * from Pokemon;
        all_pokemon = Pokemon.objects.all()
        print(all_pokemon)
        serialized_pokemon = serialize("json",all_pokemon)
        workable_pokemon = json.loads(serialized_pokemon)
        for pokemon in range(len(workable_pokemon)):
            current_pokemon = workable_pokemon[pokemon]
            list_of_moves = current_pokemon["fields"]["moves"]
            workable_list_of_moves = []
            for move in list_of_moves:
                #Select * from move where id = move name;
                my_move = Move.objects.get(id = move)
                workable_move = json.loads(serialize("json", [my_move]))
                workable_list_of_moves.append(workable_move)
            current_pokemon["fields"]["moves"] = workable_list_of_moves
        return Response(workable_pokemon)
    
class Single_Pokemon(APIView):

    def get(self, request, pokemon_name):
        # print(pokemon_name)
        pokemon = None
        try:
            pokemon = Pokemon.objects.get(name = pokemon_name.title())
        except:
            pokemon = Pokemon.objects.get(id = pokemon_name)
        pokemon = json.loads(serialize('json', [pokemon]))[0]
        list_of_moves = pokemon["fields"]["moves"]
        # print(list_of_moves)
        workable_list_of_moves = []
        for move in list_of_moves:
                #Select * from move where id = move name;
            my_move = Move.objects.get(id = move)
            workable_move = json.loads(serialize("json", [my_move]))
            workable_list_of_moves.append(workable_move)
        pokemon["fields"]["moves"] = workable_list_of_moves
        return Response(pokemon)
        