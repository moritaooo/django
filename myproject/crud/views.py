from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from .models import Product
from .forms import ProductForm


# class TopView(TemplateView):
#     template_name = "top.html"



# class ProductListView(ListView):
#     model = Product
#     paginate_by = 3


# Top
from django.views import View

class TopView(View):

    def get(self, request, *args, **kwargs):
        print('TopView!!')
        
        return render(request, "top.html")
    

class ProductListView(View):
    def get(self, request, *args, **kwargs):

        products = Product.objects.all()

        # products = Product.objects.filter(id=1)

        context = {"object_list": products}
        return render(request, "crud/product_list.html", context)
    
    def post(self, request, *args, **kwargs):
        print("Productの追加")
        """
        product = Product()
        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.save()
        return render(request, "crud/product_list.html")
        """
        form = ProductForm(request.POST)

        if form.is_valid():
            print("バリデーションルールに則っている")
            form.save()
        else:
            print("バリデーションルールに則っていない")
            print(form.errors)

        # return render(request, "crud/product_list.html")
        return redirect("crud")
        # return redirect()


class ProductUpdateView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'crud/product_update.html')

    def post(self):
        pass