from django.test import TestCase, Client
from django.urls import reverse
from plantsapi.models import Plant, Request
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.single_url = reverse('single', args=['some-slug'])
        self.plant = Plant.objects.create(
            name = 'plant',
            description = 'a very cool plant',
            image = './media/plants/boston_fern.jpeg',
            instructions = 'this is how you look after the plant',
            slug = 'some-slug'
        )
        
        self.req_url = self.list_url = reverse('req')
     

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_project_single_GET(self):
        response = self.client.get(self.single_url)
        self.assertEquals(response.status_code, 200)

    def test_project_req_GET(self):
        response = self.client.get(self.req_url)
        self.assertEquals(response.status_code, 200)

    def test_project_req_POST_correct(self):
        response = self.client.post(self.req_url, {
            'plant_name' : 'cactus'
        })
        self.assertEquals(response.status_code, 201)

    def test_project_req_POST_no_data(self):
        response = self.client.post(self.req_url, {
            'plant_name' : ''
        })
        self.assertEquals(response.status_code, 400)
        


