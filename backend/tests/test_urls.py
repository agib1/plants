from django.test import SimpleTestCase
from django.urls import reverse, resolve
from plantsapi.views import PlantsView, PlantDetail, RequestsView

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func.view_class, PlantsView)

    def test_single_url_is_resolved(self):
        url = reverse('single', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PlantDetail)

    def test_request_url_is_resolved(self):
        url = reverse('req')
        self.assertEquals(resolve(url).func.view_class, RequestsView)
