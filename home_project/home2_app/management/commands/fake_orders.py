import datetime
import random

from django.core.management.base import BaseCommand

from home2_app.models import Product, Client, Order


class Command(BaseCommand):
    help = "Generate fake orders ."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()
        products = Product.objects.all()
        for _ in range(count):
            client = random.choice(clients)
            order = Order.objects.create(client=client)
            num_products = random.randint(1, 5)  # Случайное количество товаров в заказе
            selected_products = random.sample(list(products), num_products)
            cost = 0
            for product in selected_products:
                order.product.add(product)
                cost += product.price
            order.total_price = cost
            order.save()
        self.stdout.write(f'{count} orders  added in databases')