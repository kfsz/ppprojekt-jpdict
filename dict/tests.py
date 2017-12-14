from django.test import TestCase
from django.urls import reverse
from .models import Word, WordTL
from django.http import HttpResponse, HttpResponseRedirect

# Create your tests here.

class WordIndexViewTests(TestCase):
    def test_no_words(self):
        response = self.client.get(reverse('dict:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['word_list'], [])
        
    def test_random_404(self):
        response = self.client.get(reverse('dict:detail', args=['ąę']))
        self.assertEqual(response.status_code, 404)
        
class SearchBasicRegex(TestCase):
    def test_search(self):
        response =  HttpResponseRedirect('/s/*?*')
        self.assertEqual(response.status_code, 302)
