import random

from django.core.management.base import BaseCommand

from home2_app.models import Product, Client


class Command(BaseCommand):
    help = "Generate fake clients ."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'mail{i}@mail.ru', phone_number=f"+79{''.join([str(random.randint(1,9)) for _ in range(9)])}",
                            address=f"{str(i) * 6},f'Moscow, Lenina str,{random.randint(1, 100)}")
            client.save()
        for j in range(1, count + 1):
            goods = Product(name=f'Product{j}',
                            description=f'description of  {j} is bla bla bla many long text',
                            price=random.randint(100, 2500), quantu=random.randint(1, 75))
            goods.save()
        self.stdout.write(f'Client added  and products added')
