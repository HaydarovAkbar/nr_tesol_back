from modeltranslation.translator import TranslationOptions, register
from ..models import Planners


@register(Planners)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')