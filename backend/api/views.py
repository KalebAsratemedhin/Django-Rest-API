from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}

    if instance:
        data = ProductSerializer(instance).data

    return Response(data)