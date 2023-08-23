from django.core.management.base import BaseCommand

from home2_app.models import Client


class Command(BaseCommand):
    help = "Get all user"

    def handle(self, *args, **options):
        client = Client.objects.all()
        self.stdout.write(f'{client}')
