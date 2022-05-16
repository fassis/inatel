from unittest.mock import patch

from coreapp.tests.base import BaseTestCase as TestCase
from covidapi.api import CovidAPI


def mocked_requests_valid_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({'cod': '200', 'data': 'success'}, 200)


def mocked_requests_invalid_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({'cod': '400', 'data': 'insuccess'}, 400)


class CovidAPITest(TestCase):
    def setUp(self):
        self.api = CovidAPI()

    def test_has_url_as_constant(self):
        self.assertTrue(hasattr(self.api, 'URL'))

    def test_build_url(self):
        url = self.api._CovidAPI__build_url_by_state('al')
        expected_url = '{}/brazil/uf/{}'.format(CovidAPI.URL, 'al')
        self.assertEqual(url, expected_url)

    @patch('covidapi.api.requests.get', mocked_requests_valid_get)
    def test_valid_request(self):
        response = self.api.request('sp')
        self.assertTrue('data' in response.keys())

    @patch('covidapi.api.requests.get', mocked_requests_invalid_get)
    def test_invalid_request(self):
        response = self.api.request('sp')
        self.assertTrue('error' in response.keys())
        self.assertTrue('status_code' in response.keys())