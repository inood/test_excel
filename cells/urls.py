from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CellViewSet


router = DefaultRouter()


router.register('cells', CellViewSet, basename='cell')


urlpatterns = [
    path('v1/', include(router.urls))
]
