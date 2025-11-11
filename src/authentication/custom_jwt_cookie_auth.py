from typing import Optional, Tuple, Any
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT authentication class for DRF that retrieves the access token from cookies.
    Returns a tuple of (user, validated_token) if authentication succeeds, otherwise None.
    """

    def authenticate(self, request) -> Optional[Tuple[Any, Any]]:
        access_token = request.COOKIES.get('access')
        if not access_token:
            return None
        validated_token = self.get_validated_token(access_token)
        return self.get_user(validated_token), validated_token
