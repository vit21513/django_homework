import queue

from django.contrib import admin
from home2_app.models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    fields = ['name', 'email', 'phone_number', 'address', 'data_registration']
    readonly_fields = ['data_registration']


@admin.action(description="Все по 100 руб")
def set_price(modeladmin, request, queryset):
    queryset.update(price=100)


class ProductAdmin(admin.ModelAdmin):
    """ продукты """
    actions = [set_price]
    list_display = ['name', 'description', "price", 'quantu']
    ordering = ['quantu']
    list_filter = ['data_adding', 'price', 'quantu']
    search_fields = ['quantu', 'description']
    search_help_text = 'Поиск по полю Описание продукта либо по полю количество'
    readonly_fields = ['data_adding', 'image']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Количество и его подробное описание',
                'fields': ['price', 'description', 'quantu', 'data_adding']
            },
        ),
        (
            'Изображение пордукта',
            {
                'fields': ['image'],
            }
        ),

    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price']
    fields = ['client', 'product', 'total_price', 'data_order']
    readonly_fields = ['data_order']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
