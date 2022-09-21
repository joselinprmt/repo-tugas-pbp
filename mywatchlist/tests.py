from django.test import TestCase


# Test untuk menguji bahwa url dapat mengembalikan respon HTTP 200 OK.
class BasicTest(TestCase):
    def test_mywatchlist_is_ok(self):
        response = self.client.get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)

    def test_html_is_ok(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_xml_is_ok(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json_is_ok(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
