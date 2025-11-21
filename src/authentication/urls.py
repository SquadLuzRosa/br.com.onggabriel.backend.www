from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from authentication.views import CookieTokenObtainPairView, CookieTokenRefreshView, LogoutView, UserMeView

urlpatterns = [
    path('auth/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/me/', UserMeView.as_view(), name='user_me'),
]
