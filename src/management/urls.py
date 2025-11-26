from django.urls import path, include
from rest_framework.routers import DefaultRouter

from management.views import (
    PresentationSectionViewSet,
    MissionSectionViewSet,
    DonateSectionViewSet,
    StatsCardViewSet,
    VolunteerSectionViewSet,
    DepoimentCardViewSet,
    ActivityCardViewSet,
    ContactSectionViewSet,
    TributeSectionViewSet,
    HomePageViewSet,
)

router = DefaultRouter()
router.register(r'cms/home/presentation', PresentationSectionViewSet, basename='presentation-section')
router.register(r'cms/home/mission', MissionSectionViewSet, basename='mission-section')
router.register(r'cms/home/donate', DonateSectionViewSet, basename='donate-section')
router.register(r'cms/home/stats', StatsCardViewSet, basename='stats-card')
router.register(r'cms/home/volunteer', VolunteerSectionViewSet, basename='volunteer-section')
router.register(r'cms/home/depoiments', DepoimentCardViewSet, basename='depoiment-card')
router.register(r'cms/home/activities', ActivityCardViewSet, basename='activity-card')
router.register(r'cms/home/contact', ContactSectionViewSet, basename='contact-section')
router.register(r'cms/home/tribute', TributeSectionViewSet, basename='tribute-section')
router.register(r'cms/home', HomePageViewSet, basename='home-page')

urlpatterns = [
    path('', include(router.urls))
]
