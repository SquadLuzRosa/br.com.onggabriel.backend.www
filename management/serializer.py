from rest_framework import serializers
from .models import (
    HomeSection,
    MediaSection,
    MissionSection,
    AgendaSection,
    DonationSection,
    VoluntarySection
)


class HomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSection
        fields = '__all__'


class MediaSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaSection
        fields = '__all__'


class MissionSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionSection
        fields = '__all__'


class AgendaSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaSection
        fields = '__all__'


class DonationSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationSection
        fields = '__all__'


class VoluntarySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoluntarySection
        fields = '__all__'
