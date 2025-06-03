from django.urls import path
from .views import TestimonialViewSet


urlpatterns = [
    path(
        'testimonial/', TestimonialViewSet.as_view(
            {'get': 'list', 'post': 'create'}
        ),
        name='testimonial-list'
    )
]
