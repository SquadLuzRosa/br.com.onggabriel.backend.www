from dj_rql.filter_cls import AutoRQLFilterClass
from .models import CustomUser


class CustomUserFilterClass(AutoRQLFilterClass):
    MODEL = CustomUser
