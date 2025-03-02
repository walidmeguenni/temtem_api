from django.urls import path
from .views import getUsers, getUser, updateUser, deleteUser

urlpatterns = [
    path('', getUsers, name='get_users'),
    path('update/<int:pk>', updateUser, name='update_user'),
    path('delete/<int:pk>', deleteUser, name='delete_user'),
    path('<int:pk>', getUser, name='get_user'),
]