from django.core.management.base import BaseCommand

from home2_app.models import Client


class Command(BaseCommand):
    help = "Get all clients"

    def handle(self, *args, **options):
        client = Client.objects.all()
        self.stdout.write(f'{client}')
