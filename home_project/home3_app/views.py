import datetime
import operator
from django.http import HttpResponse
from django.shortcuts import render

from home2_app.models import Client, Order


# Create your views here.


def index(request):
    return HttpResponse("""<h1>home Work 3</h1> """)


def orders_by_user_name(request, name):
    client = Client.objects.filter(name=name).first()
    if client:
        orders = Order.objects.filter(client=client).all()
        now = datetime.datetime.now()
        week = now - datetime.timedelta(days=7)
        month = now - datetime.timedelta(days=30)
        year = now - datetime.timedelta(days=365)
        not_orders_week = Order.objects.filter(client=client, data_order__gte=week, data_order__lte=now).order_by(
            '-data_order')
        orders_week= sorted(not_orders_week, key=operator.attrgetter('data_order'))
        not_orders_month = Order.objects.filter(client=client, data_order__gte=month, data_order__lte=now).order_by(
            '-data_order')
        orders_month = sorted(not_orders_month, key=operator.attrgetter('data_order'))
        not_orders_year = Order.objects.filter(client=client, data_order__gte=year, data_order__lte=now).order_by(
            '-data_order')
        orders_year = sorted(not_orders_year, key=operator.attrgetter('data_order'))
        context = {"name_client": name, "client": orders, "orders_week": orders_week, "orders_month": orders_month,
                   "orders_year": orders_year}
    else:
        context = {"name_client": "not found", "client": "not found", "orders_week": "not found",
                   "orders_month": "not found",
                   "orders_year": "not found"}

    return render(request, "home3_app/app3.html", context)
