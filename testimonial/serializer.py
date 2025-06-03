from .models import Depoiment as Testimonial
from rest_framework.serializers import ModelSerializer


class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
