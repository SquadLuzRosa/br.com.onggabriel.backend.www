from django.urls import path, include
from rest_framework.routers import DefaultRouter

from testmonial.views import DepoimentModelViewSet, FunctionModelViewSet

router = DefaultRouter()
router.register(r'depoiment', DepoimentModelViewSet, basename='depoiment')
router.register(r'function', FunctionModelViewSet, basename='function')

urlpatterns = [
    path('', include(router.urls))
]
