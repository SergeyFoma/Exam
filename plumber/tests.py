from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

class GetPagesTestCase(TestCase):
    def setUp(self):
        "Инициализация перед выполнением каждого теста"
    
    def test_index(self):
        path=reverse('plumber:index')
        response=self.client.get(path)
        #print(response)
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        #self.assertIn('plumber/index.html', response.template_name)
        self.assertTemplateUsed(response, 'plumber/index.html')
        self.assertEqual(response.context_data['title'],'Test online. Тестирование работников основных и смежных профессий')

    # def test_redirect_logout(self):
    #     path=reverse("users:logout_user")


    def tearDown(self):
        "Действие после выполнения каждого теста"

# Create your tests here.
