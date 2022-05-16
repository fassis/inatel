import datetime

from coreapp.tests.base import BaseTestCase as TestCase
from coreapp.models import HealthUnityFile


class HealthUnityFileModelTest(TestCase):
    def setUp(self):
        self.health_unity_file = HealthUnityFile.objects.create(
            file='path/to/file.csv',
        )

    def test_create(self):
        self.assertTrue(HealthUnityFile.objects.exists())
    
    def test_str(self):
        self.assertEqual('{}'.format(self.health_unity_file.pk),
        str(self.health_unity_file))

    def test_created_at(self):
        self.assertIsInstance(self.health_unity_file.created_at,
        datetime.datetime)