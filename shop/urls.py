from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('search/', search, name='search'),
    path('all/', show_all, name='show_all'),
    path('product/<int:art>/', show_product, name='show_product'),
    path('order/<int:art>/', order, name='order'),
]


