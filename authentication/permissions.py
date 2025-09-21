from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class PublicReadAndCSRFCheckPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        csrf_token_cookie = request.COOKIES.get('XSRF-TOKEN')
        csrf_token_header = request.headers.get('X-CSRF-Token')

        if not csrf_token_cookie or not csrf_token_header or csrf_token_header != csrf_token_cookie:
            raise PermissionDenied('CSRF Verification Failed.')

        return True
