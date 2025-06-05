from dj_rql.filter_cls import AutoRQLFilterClass
from .models import (
    Post,
    CategoryType,
    Tag,
    EngagementMetrics,
    Media
)


class PostFilterClass(AutoRQLFilterClass):
    MODEL = Post


class CategoryTypeFilterClass(AutoRQLFilterClass):
    MODEL = CategoryType


class TagFilterClass(AutoRQLFilterClass):
    MODEL = Tag


class EngagementMetricsFilterClass(AutoRQLFilterClass):
    MODEL = EngagementMetrics


class MediaFilterClass(AutoRQLFilterClass):
    MODEL = Media
