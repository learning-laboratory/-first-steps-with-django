from django.shortcuts import get_object_or_404, render
from .models import Product
from .forms import ProductForm, RawProductForm

# def product_create_view(request):
#     print(request.GET['name'])
#     print(request.POST.get("name"))
#     context = {}
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#       #  form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def render_initial_data(request):
    initial_data = {
        'name': "New Name"
    }
    product = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance = product)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_detail_view(request):
#     product = Product.objects.get(id=1)
#     context = {
#         "product": product
#     }
#     return render(request, "products/product_detail.html", context)

def dynamic_lookup_view(request, id):
    product = Product.objects.get(id = id)
    context = {
       "product": product 
    }
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            # The data is good
            print(form.cleaned_data)
            Product.objects.create(
                **form.cleaned_data
            )
        else:
            print(form.errors)

    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request, id):
    product = Product.objects.get(id = id)
    context = {
       "product": product 
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
    context = {
       "product": product 
    }
    return render(request, "products/product_delete.html", context)

def product_update_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.save()
    context = {
       "product": product 
    }
    return render(request, "products/product_update.html", context)

def product_list_view(request):
    products = Product.objects.all()
    context = {
       "products": products
    }
    return render(request, "products/product_list.html", context)
