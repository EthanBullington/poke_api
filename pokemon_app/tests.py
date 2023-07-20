from django.test import TestCase
from .models import Pokemon
from django.core.exceptions import ValidationError

# Create your tests here.
class pokemon_test(TestCase):
    def test_01_create_pokemon_instance(self):
        new_pokemon = Pokemon(name = "Charmander", description = 'this is charmander, it looks like a piece of lettuce')
        try:
            new_pokemon.full_clean() #Necessary for validators to run on new instances
            #if model cannot be created due to validators new_pokemon = None
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e: #Allows us to print out the error message, however it is not needed for creating test cases.
            print(e.message_dict)
            self.fail()

    def test_02_create_pokemon_instance(self):
        new_pokemon = Pokemon(name = "12343214352", description = 'Mwahahaha this is a bad pokemon, with more than 25 letters')
        try:
            new_pokemon.full_clean() #Necessary for validators to run on new instances
            #if model cannot be created due to validators new_pokemon = None
            self.fail()
            

        except ValidationError as e: #Allows us to print out the error message, however it is not needed for creating test cases.
            # print(e.message_dict)
            self.assert_('Improper name format' in e.message_dict['name'])
            