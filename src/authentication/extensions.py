from drf_spectacular.extensions import OpenApiAuthenticationExtension

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
