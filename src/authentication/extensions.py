from drf_spectacular.extensions import OpenApiAuthenticationExtension
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.custom_jwt_cookie_auth import CustomJWTAuthentication


class CustomJWTCookieAuthScheme(OpenApiAuthenticationExtension):
    target_class = CustomJWTAuthentication
    name = 'custom_jwt_cookie'

    def get_security_definition(self, auto_schema):
        return {
            'type': 'apiKey',
            'in': 'cookie',
            'name': 'access'
        }


class SimpleJWTScheme(OpenApiAuthenticationExtension):
    target_class = JWTAuthentication
    name = "jwt_default"

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
        }
