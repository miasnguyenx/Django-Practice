from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:order_id>/', views.details, name='details'),
    path('orders', views.orders, name='orders'),
]