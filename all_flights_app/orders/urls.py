from rest_framework.routers import DefaultRouter
from all_flights_app.orders.views import OrdersViewSet, calc_sum
from django.urls import path

router = DefaultRouter()
router.register('', OrdersViewSet)

urlpattens = [
    path('calc',calc_sum)
]

urlpattens.extend(router.urls)

