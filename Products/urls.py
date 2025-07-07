from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.index, name = "products"),
    path('products/<int:cat_id>/', views.index, name='products_by_category'),  # С категорией
    path('about-us/', views.about, name="about"),
    path('basket/', views.basket, name = "basket"),
]
