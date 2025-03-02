from rest_framework.response import Response
from rest_framework.decorators import api_view

from authentication.middleware import jwt_auth_required
from .models import User
from .serializers import UserSerializer
from django.http import Http404

@api_view(['GET'])
@jwt_auth_required
def getUsers(request):
    try:
        if not request.user.role == 'owner':
            return Response({'error': 'Unauthorized'}, status=401)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@jwt_auth_required
def getUser(request, pk):
    try:
        if not request.user.role == 'owner' and request.user.id != pk:
            return Response({'error': 'Unauthorized'}, status=401)
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        raise Http404('User not found')
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['PUT'])
@jwt_auth_required
def updateUser(request, pk):
    try:
        if not request.user.role == 'owner' and request.user.id != pk:
            return Response({'error': 'Unauthorized'}, status=401)
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except User.DoesNotExist:
        raise Http404('User not found')
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
@jwt_auth_required
def deleteUser(request, pk):
    try:
        if not request.user.role == 'owner' and request.user.id != pk:
            return Response({'error': 'Unauthorized'}, status=401)
        user = User.objects.get(id=pk)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=204)
    except User.DoesNotExist:
        raise Http404('User not found')
    except Exception as e:
        return Response({'error': str(e)}, status=500)
