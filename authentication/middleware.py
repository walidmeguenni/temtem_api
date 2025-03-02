import jwt
from django.http import JsonResponse
from functools import wraps
from temtem_api import settings
from user.models import User

def jwt_auth_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and ' ' in auth_header:
            try:
                parts = auth_header.split(' ')
                if len(parts) == 2 and parts[0] == 'Bearer':
                    token = parts[1]
                    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                    user = User.objects.get(id=payload['id'])
                    request.user = user  # Attach user to request
                    return view_func(request, *args, **kwargs)
            except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
                return JsonResponse({'error': 'Unauthorized'}, status=401)
        return JsonResponse({'error': 'Invalid or missing token'}, status=401)
    return _wrapped_view
