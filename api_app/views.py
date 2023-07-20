from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
from rest_framework.views import APIView
from rest_framework.response import Response
import pprint
from dotenv import dotenv_values

env = dotenv_values(".env")
pp = pprint.PrettyPrinter(indent=2, depth=2)

class Noun_project(APIView):

    def get(self, request, item):
        auth = OAuth1(env.get('API_KEY'), env.get('SECRET_KEY')) # get key from api, this is Francisco
        endpoint = f"https://api.thenounproject.com/icon/{item}/"
        response = requests.get(endpoint, auth=auth)
        print(env)
        JSONresponse = response.json()
        # pp.pprint(JSONresponse)
        icon_url = JSONresponse.get('icon').get('icon_url') #using .get instead og [] to allow it to continue to work
        # print(icon_url)
        return Response(icon_url)
