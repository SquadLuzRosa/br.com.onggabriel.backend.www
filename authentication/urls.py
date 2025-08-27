from django.urls import path
from .views import CookieTokenObtainPairView, CookieTokenRefreshView, LogoutView
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('auth/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]
