from django.core.management.base import BaseCommand

from home2_app.models import Client


class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        parser.add_argument('pk',type=int, help="User_id")

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        if  client is not None:
            client.delete()
        self.stdout.write(f'{client}')
