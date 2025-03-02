from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.http import Http404
from authentication.middleware import jwt_auth_required


@api_view(['GET'])

def getProducts(request):
    try:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@jwt_auth_required
def getProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        raise Http404('Product not found')
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
@jwt_auth_required
def createProduct(request):
    try:
        if not request.user.role == 'owner':
            return Response({'error': 'Unauthorized'}, status=401)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['PUT'])
@jwt_auth_required
def updateProduct(request, pk):
    try:
        if not request.user.role == 'owner':
            return Response({'error': 'Unauthorized'}, status=401)
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Product.DoesNotExist:
        raise Http404('Product not found')
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
@jwt_auth_required
def deleteProduct(request, pk):
    try:
        if not request.user.role == 'owner':
            return Response({'error': 'Unauthorized'}, status=401)
        product = Product.objects.get(id=pk)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=204)
    except Product.DoesNotExist:
        raise Http404('Product not found')
    except Exception as e:
        return Response({'error': str(e)}, status=500)
