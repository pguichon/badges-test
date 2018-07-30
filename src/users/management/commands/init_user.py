from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a test User"

    def handle(self, *args, **options):
        """
        create a User like test and a superuser
        """
        User.objects.create_user('test', 'test@toto.fr', 'password')
        User.objects.create_superuser('admin', 'admin@toto.fr', 'password')
        print('users created')
