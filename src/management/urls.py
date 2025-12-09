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
    AboutHistorySectionViewSet,
    AboutMissionSectionViewSet,
    AboutValueCardsViewSet,
    AboutIdealizersSectionViewSet,
    AboutCarouselSectionViewSet,
    AboutPageViewSet,
)

router = DefaultRouter()

# Home page routes
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

# About page routes
router.register(r'cms/about/history', AboutHistorySectionViewSet, basename='about-history-section')
router.register(r'cms/about/mission', AboutMissionSectionViewSet, basename='about-mission-section')
router.register(r'cms/about/values', AboutValueCardsViewSet, basename='about-value-cards')
router.register(r'cms/about/idealizers', AboutIdealizersSectionViewSet, basename='about-idealizers-section')
router.register(r'cms/about/carousel', AboutCarouselSectionViewSet, basename='about-carousel-section')
router.register(r'cms/about', AboutPageViewSet, basename='about-page')

urlpatterns = [
    path('', include(router.urls))
]
