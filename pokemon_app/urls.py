from django.urls import path, register_converter
from .views import All_Pokemon, Single_Pokemon
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, "int_or_str")

urlpatterns = [
    path('', All_Pokemon.as_view(), name='all_pokemon'),
    path("<int_or_str:pokemon_name>/", Single_Pokemon.as_view(), name='single_pokemon')
]