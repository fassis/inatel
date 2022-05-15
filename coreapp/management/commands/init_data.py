from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create the initial admin.'

    def handle(self, *args, **options):
        get_user_model().objects.create_superuser(
            'admin', 
            'a@a.com', 
            'admin')