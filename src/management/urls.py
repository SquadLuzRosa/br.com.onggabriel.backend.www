from django.urls import path, include
from rest_framework.routers import DefaultRouter

from management.views import (
    PresentationSectionViewSet,
    MissionSectionViewSet,
    DonateSectionViewSet,
    StatsCardViewSet,
    VolunteerSectionViewSet,
    DepoimentCardViewSet,
    ContactSectionViewSet,
    TributeSectionViewSet,
)

router = DefaultRouter()
router.register(r'home/presentation', PresentationSectionViewSet, basename='presentation-section')
router.register(r'home/mission', MissionSectionViewSet, basename='mission-section')
router.register(r'home/donate', DonateSectionViewSet, basename='donate-section')
router.register(r'home/stats', StatsCardViewSet, basename='stats-card')
router.register(r'home/volunteer', VolunteerSectionViewSet, basename='volunteer-section')
router.register(r'home/depoiments', DepoimentCardViewSet, basename='depoiment-card')
router.register(r'home/contact', ContactSectionViewSet, basename='contact-section')
router.register(r'home/tribute', TributeSectionViewSet, basename='tribute-section')

urlpatterns = [
    path('', include(router.urls))
]
