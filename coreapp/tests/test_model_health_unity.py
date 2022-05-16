import datetime

from coreapp.tests.base import BaseTestCase as TestCase
from coreapp.models import HealthUnityFile, HealthUnity


class HealthUnityFileTest(TestCase):
    def setUp(self):
        file = HealthUnityFile.objects.create(
            file='path/to/file.csv',
        )

        self.health_unity = HealthUnity.objects.create(
            file=file,
            cnes_code=11,
            ibge_uf=22,
            ibge_city=33333,
            name='Test name',
            address='Test Address',
            district='Test District',
            lat=10.111111,
            lon=35.111111,
        )

    def test_create(self):
        self.assertTrue(HealthUnity.objects.exists())

    def test_str(self):
        self.assertEqual('{}'.format(self.health_unity.name),
        str(self.health_unity))

    def test_created_at(self):
        self.assertIsInstance(self.health_unity.created_at,
        datetime.datetime)