from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Events


class EventsFilterClass(AutoRQLFilterClass):
    MODEL = Events
