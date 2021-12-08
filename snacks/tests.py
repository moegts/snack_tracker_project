  
from django.test import TestCase 
from django.urls import reverse

# Create your tests here.

class SnacksTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse('snack_list')
        actual_status_code = self.client.get(url).status_code
        self.assertEqual(actual_status_code, 200)


    def test_list_page_templete(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')



   
