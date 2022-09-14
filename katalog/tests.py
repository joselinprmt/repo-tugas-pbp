from django.test import TestCase
from django.urls import reverse, resolve
from katalog.models import CatalogItem
from katalog.views import show_katalog

# Create your tests here.
class BasicTest(TestCase):
    def test_models_is_working(self):
        barang = CatalogItem()
        barang.item_name = "Barang 1"
        barang.item_price = 999999999
        barang.item_stock = 99
        barang.description = "Ini deskripsi barang"
        barang.rating = 5
        barang.item_url = "https://www.tokopedia.com/ptpratamasemesta/iphone-12-pro-max-garansi-resmi-ibox-silver-256-gb"
        barang.save()

        record = CatalogItem.objects.get(pk=1)
        self.assertEqual(record, barang)

    def test_url_is_showing_the_correct_view(self):
        link = reverse('katalog:show_katalog')
        self.assertEqual(resolve(link).func, show_katalog)
