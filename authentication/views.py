from rest_framework.response import Response
from rest_framework.decorators import api_view
from temtem_api import settings
from user.models import User
from django.contrib.auth.hashers import make_password, check_password
import jwt
from datetime import datetime, timedelta

@api_view(['POST'])
def register(request):
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'All fields are required'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=400)

        User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )

        return Response({'message': 'User created successfully'}, status=201)

    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
def login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=400)

        user = User.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            payload = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'exp': datetime.utcnow() + timedelta(days=1)
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
            return Response({'token': token, 'user': user_data})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

    except Exception as e:
        return Response({'error': str(e)}, status=500)
