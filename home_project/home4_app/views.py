from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from home2_app.models import Product
from home4_app.form import Product_form, Product_add_foto


def creaty_product(request):
    mesage = ''
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantu = form.cleaned_data['quantu']
            image = form.cleaned_data['image']
            product = Product.objects.create(name=name,
                                             description=description,
                                             price=price,
                                             quantu=quantu,
                                             image=image)
            product.save()
            mesage = "Продукт добавлен"
    else:
        mesage = ""
        form = Product_form()
    return render(request, 'home4_app/creaty_product.html', {'form': form, 'mesage': mesage})


def add_photo(request):
    mesage = ''
    if request.method == 'POST':
        form = Product_add_foto(request.POST, request.FILES)
        if form.is_valid():
            product = form.cleaned_data['product']
            image = form.cleaned_data['image']
            product.image = image
            product.save()
            mesage = "В Продукт добавлено фото "
    else:
        mesage = ""
        form = Product_add_foto()
    return render(request, 'home4_app/add_image_product.html', {'form': form, 'mesage': mesage})
