from django.urls import path
from user import views

urlpatterns = [
    path('', views.get_users, name='get_users'),
    path('<id>', views.get_user_by_id, name='get_user_by_id'),
    path('create', views.create_user, name='create_user'),
    path('update', views.update_user, name='update_user'),
    path('delete', views.delete_user, name='delete_user')
     
]
