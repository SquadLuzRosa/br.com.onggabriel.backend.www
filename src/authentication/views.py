import secrets

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from authentication.serializers import UserSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    """
    View to obtain JWT access and refresh tokens and set them in cookies.
    Also sets a CSRF token in a cookie for double submit protection.
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to obtain JWT tokens and set them in cookies.
        Returns a response with a CSRF token and success message.
        """
        response = super().post(request, *args, **kwargs)
        data = getattr(response, 'data', None)
        if data is None:
            return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
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
            path='/',
        )

        response.set_cookie(
            key='refresh',
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite='None',
            max_age=60 * 60 * 24 * 7,
            path='/',
        )

        response.set_cookie(
            key='XSRF-TOKEN',
            value=csrf_token,
            httponly=False,
            secure=True,
            samesite='None',
            path='/',
        )

        response.data = {'detail': 'Login Efetuado Com Sucesso', 'xsrfToken': csrf_token}
        return response


class CookieTokenRefreshView(TokenRefreshView):
    """
    View to refresh JWT access token using the refresh token from cookies.
    Validates CSRF token before refreshing.
    """

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to refresh the JWT access token.
        Validates CSRF token and sets new access and CSRF tokens in cookies.
        """
        refresh_token = request.COOKIES.get('refresh')
        csrf_token_cookie = request.COOKIES.get('XSRF-TOKEN')
        csrf_token_header = request.headers.get('X-XSRF-TOKEN')

        if (
            not csrf_token_cookie
            or not csrf_token_header
            or csrf_token_cookie != csrf_token_header
        ):
            return Response(
                {'detail': 'CSRF Token Validation Failed'}, status=status.HTTP_401_UNAUTHORIZED
            )
        if not refresh_token:
            return Response(
                {'detail': 'Refresh Token Missing'}, status=status.HTTP_401_UNAUTHORIZED
            )
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
                path='/',
            )
            new_csrf_token = secrets.token_urlsafe(32)
            response.set_cookie(
                key='XSRF-TOKEN',
                value=new_csrf_token,
                httponly=False,
                secure=True,
                samesite='None',
                path='/',
            )
            return response
        except Exception:
            return Response(
                {'detail': 'Invalid Refresh Token'}, status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):
    """
    View to handle user logout by deleting authentication and CSRF cookies.
    """

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to log out the user and delete cookies.
        """
        response = Response({'detail': 'Logout Realizado com Sucesso'}, status=status.HTTP_200_OK)

        response.delete_cookie('access')
        response.delete_cookie('refresh')
        response.delete_cookie('XSRF-TOKEN')

        return response


class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
