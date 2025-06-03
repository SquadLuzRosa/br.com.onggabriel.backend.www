from .serializer import TestimonialSerializer
from rest_framework import viewsets
from .models import Depoiment as Testimonial


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
