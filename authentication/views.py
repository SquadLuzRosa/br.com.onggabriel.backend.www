from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import secrets


class CookieTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data
        access_token = data.get('access')
        refresh_token = data.get('refresh')

        if not access_token or not refresh_token:
            return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        csrf_token = secrets.token_urlsafe(32)
        response.set_cookie(
            key='access',
            value=access_token,
            httponly=True,
            secure=True,
            samesite='None',
            max_age=60 * 5,
            path='/'
        )

        response.set_cookie(
            key='refresh',
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite='None',
            max_age=60 * 60 * 24 * 7,
            path='/'
        )

        response.set_cookie(
            key='XSRF-TOKEN',
            value=csrf_token,
            httponly=False,
            secure=True,
            samesite='None',
            path='/'
        )

        response.data = {'detail': 'Login Efetuado Com Sucesso'}
        return response


class CookieTokenRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')
        csrf_token_cookie = request.COOKIES.get('XSRF-TOKEN')
        csrf_token_header = request.headers.get('X-XSRF-TOKEN')

        if not csrf_token_cookie or not csrf_token_header or csrf_token_cookie != csrf_token_header:
            return Response({
                'detail': 'CSRF Token Validation Faield'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        if not refresh_token:
            return Response({'detail': 'Refresh Token Missin'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            response = Response({'detail': 'Token Refreshed'}, status=status.HTTP_200_OK)
            response.set_cookie(
                key='access',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                max_age=60 * 5,
                path='/'
            )
            new_csrf_token = secrets.token_urlsafe(32)
            response.set_cookie(
                key='XSRF-TOKEN',
                value=new_csrf_token,
                httponly=False,
                secure=True,
                samesite='None',
                path='/'
            )
            return response
        except Exception:
            return Response({'detail': 'Invalid Refresh Token'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        response = Response({'detail': 'Logout Realizado com Sucesso'}, status=status.HTTP_200_OK)

        response.delete_cookie('access')
        response.delete_cookie('refresh')
        response.delete_cookie('XSRF-TOKEN')

        return response
