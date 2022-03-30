from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views


room_list = views.CustomerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


room_detail = views.CustomerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('customers/', room_list, name='room_list'),
    path('customers/<int:pk>/', room_detail, name='room-detail'),
])