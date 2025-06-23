from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('products/',views.index, name = "products"),
    ]
