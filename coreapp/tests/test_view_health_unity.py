from django.shortcuts import resolve_url as r
from coreapp.tests.base import BaseTestCase as TestCase
from coreapp.models import HealthUnity, HealthUnityFile


class HealthUnityFileDetailGet(TestCase):
    def setUp(self):
        super(HealthUnityFileDetailGet, self).setUp()

        self.health_unity_file = HealthUnityFile.objects.create(
            file='path/to/file.csv',
        )
        self.health_unity = HealthUnity.objects.create(
            file=self.health_unity_file,
            cnes_code=11,
            ibge_uf=22,
            ibge_city=33333,
            name='Test name',
            address='Test Address',
            district='Test District',
            lat=10.111111,
            lon=35.111111,
        )
        self.response = self.client.get(
            r('coreapp:health_unity_file_detail', self.health_unity_file.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'app/ubs_detail.html')

    def test_context(self):
        variables = ['unities_file', 'unities']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)


class HealthUnityFileListGet(TestCase):
    def setUp(self):
        super(HealthUnityFileListGet, self).setUp()
        self.health_unity_file = HealthUnityFile.objects.create(
            file='path/to/file.csv',
        )
        self.response = self.client.get(r('coreapp:health_unity_file_list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'app/ubs_file_list.html')

    def test_html(self):
        content = [
            ('path/to/file.csv'),
        ]

        for expected in content:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context(self):
        variables = ['unity_files']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)