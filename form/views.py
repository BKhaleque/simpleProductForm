from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, JsonResponse
from .models import  Product
from django.template import RequestContext
from .forms import ProductForm
import json
from django.views.decorators.csrf import csrf_exempt



#class ProductAddView(views.CsrfExemptMixin, vies.JsonRequestMixin, View):

 #   require_json = true
  #  page =

   # def post(self, request):


def index(request):
    return render(request, 'form/index.html')

@csrf_exempt
def products(request):
        output_list =[]
        product_list = Product.objects.all().values()
        for p in product_list:
            json_dict = {'ID': p['id'],
                         'Name': p['product_name'],
                         'Description': p['product_desc'],
                         'Price': p['product_price']}
            output_list.append(json_dict)
        if request.method == 'GET':

            return JsonResponse(output_list, safe=False,)

        elif request.method == 'DELETE':
            body = json.loads(request.body.decode('utf-8'))
            product = Product.objects.get(product_name=body['id'])
            product.delete()
            return JsonResponse(output_list, safe=False)

        elif request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            product = Product.objects.create()
            product.name = body['name']
            product.desc = body['description']
            product.price = body['price']
            product.save()
            return JsonResponse(output_list, safe=False)

        elif request.method == 'PUT':
            body = json.loads(request.body.decode('utf-8'))
            product = Product.objects.get(id=request.ID)
            product.name = body['name']
            product.description = body['description']
            product.price = body['price']
            product.save()
            data = Product.objects.all().values()
            return JsonResponse(list(data), safe=False)


def product_details(request, product_id):
    #response = "You're looking at the details of question %s."
    if request.method =='GET':
        product = get_object_or_404(Product, pk=product_id)

        return render(request, 'form/product_details.html', {'product':product})



#
#def validate_product(request):
#    product = request.GET.get('product_name', None)
#    data = {
#        'Message': Product.objects.filter(product_name=product_name).exists()
#        }
 #   return JsonResponse(data)
