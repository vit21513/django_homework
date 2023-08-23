from django.core.management.base import BaseCommand
from home2_app.models import Client


class Command(BaseCommand):
    help = "edit client  name "

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Client_name")
        parser.add_argument('new_name', type=str, help="New_Client_name")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        new_name = kwargs.get('new_name')
        client = Client.objects.filter(name=name).first()
        if client:
            client.name=new_name
            client.save()
            self.stdout.write(f'edit client{client}')
        self.stdout.write(f' clients {name} in base note found')