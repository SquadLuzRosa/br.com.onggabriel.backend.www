from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


class CustomCSRFMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            csrf_cookie = request.COOKIES.get('XSRF-TOKEN')
            csrf_header = request.headers.get('X-CSRF-Token')

            if not csrf_cookie or not csrf_header or csrf_cookie != csrf_header:
                return JsonResponse({'detail': 'CSRF verification failed'}, status=403)
            return None
