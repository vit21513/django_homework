from django.core.management.base import BaseCommand
from home2_app.models import Client


class Command(BaseCommand):
    help = "Creaty Client"

    def handle(self, *args, **options):
        client = Client(name="First", email="first@no.com",phone_number="+7911111111", address="152330, Moscow, Lenina str,20")
        client.save()
        self.stdout.write(f'Client added {client}')


