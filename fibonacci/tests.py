from django.test import TestCase
from django.test.client import Client


class ApiTestCase(TestCase):

    def test_correct_request(self):
        c = Client()
        response = c.get("/fibonachi", {'from': 1, 'to': 5})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"response":[1,1,2,3,5]}')

    def test_from_missing(self):
        c = Client()
        response = c.get("/fibonachi", {'to': 5})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{"error":"From field is required"}')

    def test_to_missing(self):
        c = Client()
        response = c.get("/fibonachi", {'from': 5})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{"error":"To field is required"}')

    def test_from_is_a_string(self):
        c = Client()
        response = c.get("/fibonachi", {'from': 'dog', 'to': 4})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{"error":"From field must be a number"}')

    def test_to_is_a_string(self):
        c = Client()
        response = c.get("/fibonachi", {'from': 1, 'to': 'cat'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{"error":"To field must be a number"}')

    def test_negative(self):
        c = Client()
        response = c.get("/fibonachi", {'from': -1, 'to': -3})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{"error":"From and to must be non-negative"}')

    def test_from_less_than_to(self):
        c = Client()
        response = c.get("/fibonachi", {'from': 10, 'to': 3})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{"error":"From value must be less or equal than to value"}')

    def test_nonexistent_url(self):
        c = Client()
        response = c.get("/")

        self.assertEqual(response.status_code, 404)
