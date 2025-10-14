from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


class PublicReadAndCSRFCheckPermission(BasePermission):
    '''
    Permissão Global: permite leitura para qualquer um (GET, HEAD, OPTIONS),
    mas exige uma validação de CSRF (Double Submit Cookie) para qualquer
    método que altere dados (POST, PUT, PATCH, DELETE).
    '''
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        csrf_token_cookie = request.COOKIES.get('XSRF-TOKEN')
        csrf_token_header = request.headers.get('X-XSRF-TOKEN')

        if not csrf_token_cookie or not csrf_token_header or csrf_token_header != csrf_token_cookie:
            raise PermissionDenied('CSRF Verification Failed.')
        return True
