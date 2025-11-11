from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


class PublicReadAndCSRFCheckPermission(BasePermission):
    """
    Global permission: allows read-only access for anyone (GET, HEAD, OPTIONS),
    but requires CSRF validation (Double Submit Cookie) for any method that modifies data
    (POST, PUT, PATCH, DELETE).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        csrf_token_cookie = request.COOKIES.get('XSRF-TOKEN')
        csrf_token_header = request.headers.get('X-XSRF-TOKEN')

        if (
            not csrf_token_cookie
            or not csrf_token_header
            or csrf_token_header != csrf_token_cookie
        ):
            raise PermissionDenied('CSRF Verification Failed.')
        return True
