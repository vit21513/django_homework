from django.core.management.base import BaseCommand

from home2_app.models import Client, Order



class Command(BaseCommand):
    help = "Get user orders by user nameget_orders.py "

    def add_arguments(self, parser):
        parser.add_argument('name',type=str, help="Client_name")

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        client = Client.objects.filter(name=name).first()
        order = Order.objects.filter(client=client).first()
        self.stdout.write(f'{order}')
