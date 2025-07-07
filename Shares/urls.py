from django.urls import path
from . import views

urlpatterns = [
    path('shares/promotions-on-goods/', views.promotion_on_goods, name="promotion-on-goods"),
    path('shares/promotions-on-goods/<int:shares_id>/', views.shares_info, name="shares-info"),
    path('shares/promotions-on-goods/<int:shares_id>/increment/', views.increment_view, name="increment_view"),

]
