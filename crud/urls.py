from django.urls import path

from . import views

app_name = 'crud'
urlpatterns = [
    # path('', views.index, name='index'),
    path('users', views.users, name='all_users'),
    path('products', views.products, name='all_products'),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('index2', views.index2.as_view(), name="APIviewCBV"),
    path('index1', views.index1, name="APIviewFBV")
]