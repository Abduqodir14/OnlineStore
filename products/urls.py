from django.urls import path, include
from products.views import *


app_name = 'products'
urlpatterns = [
    path('<int:product_id>/', product, name='product'),
]