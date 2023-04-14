from django.urls import path

from . import views

# namespace for an app --->  url crud:detail
app_name = 'crud'
urlpatterns = [
    path('', views.login, name='home'),    
    path('users', views.users, name='users'),
    path('products', views.products, name='products'),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('detail/<str:product_code>', views.detail, name="detail"),
    path('delete/<str:product_code>', views.delete, name="delete"),
    path('update/<str:product_code>', views.update, name="update"),
    path('confirmdelete/<str:product_code>', views.confirm_delete, name="confirmdelete"),
    path('index2', views.index2.as_view(), name="APIviewCBV"),
    path('index1', views.index1, name="APIviewFBV")
]