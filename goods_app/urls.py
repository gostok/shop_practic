from django.contrib import admin
from django.urls import path
from .views import *

app_name = "goods"

urlpatterns = [
    path("search/", catalog, name="search"),
    path("<slug:category_slug>/", catalog, name="catalog"),
    path("product/<slug:product_slug>/", product, name="product"),
]
