from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from django.urls import reverse
# Create your tests here.


class NounProject(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    @patch("requests.get")
    def test_noun_project(self, mock_get):
        ball = 'pokeball'
        preview_url = 'this is where the pokeball image would be' #Would normally be that URL .com
        mock_response = type('MockResponse', (), {'json': lambda self: {'icon':{'preview_url': preview_url}}})
        mock_get.return_value = mock_response()
        response = self.client.get(reverse('noun_project', args=[ball]))
        print(response.content)
        self.assertEquals(preview_url, response.json())

