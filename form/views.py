from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, JsonResponse,QueryDict
from .models import  Product
from django.template import RequestContext
from .forms import ProductForm
import json
from django.views.decorators.csrf import csrf_exempt





#class ProductAddView(views.CsrfExemptMixin, vies.JsonRequestMixin, View):

 #   require_json = true
  #  page =

   # def post(self, request):

@csrf_exempt
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
            ID = QueryDict(request.body).get('ID')
            p = Product.objects.get(pk=ID)
            p.delete()
            return JsonResponse(None, safe=False)

        elif request.method == 'POST':
            p = Product()
            p.product_name = QueryDict(request.body).get('Name')
            p.product_desc = QueryDict(request.body).get('Description')
            p.product_price = QueryDict(request.body).get('Price')
            p.save()
            return JsonResponse(p.id, safe=False)

        elif request.method == 'PUT':
            ID = QueryDict(request.body).get('ID')
            p = Product.objects.get(pk=ID)
            name = QueryDict(request.body).get('Name')
            desc = QueryDict(request.body).get('Description')
            price = QueryDict(request.body).get('Price')
            p.product_name = name
            p.product_desc = desc
            p.product_price = price
            p.save()
            output_list = serializers.serialize("json", [p])
            return JsonResponse(output_list, safe=False)

@csrf_exempt
def product_details(request, product_id):
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
