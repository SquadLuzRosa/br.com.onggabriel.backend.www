from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomeSectionViewSet,
    MediaSectionViewSet,
    AboutSectionViewSet,
    MissionSectionViewSet,
    AgendaSectionViewSet,
    DonationSectionViewSet,
    VoluntarySectionViewSet
)


router = DefaultRouter()
router.register(r'home_section', HomeSectionViewSet, basename='home_section')
router.register(r'media_section', MediaSectionViewSet, basename='media_section')
router.register(r'about_section', AboutSectionViewSet, basename='about_section')
router.register(r'mission_section', MissionSectionViewSet, basename='mission_section')
router.register(r'agenda_section', AgendaSectionViewSet, basename='agenda_section')
router.register(r'donation_section', DonationSectionViewSet, basename='donation_section')
router.register(r'voluntary_section', VoluntarySectionViewSet, basename='voluntary_section')

urlpatterns = [
    path('', include(router.urls))
]
