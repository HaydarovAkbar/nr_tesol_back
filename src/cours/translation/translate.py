from modeltranslation.translator import TranslationOptions, register
from ..models import CourseType, Courses, Teachers


@register(CourseType)
class CourseTypeTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Teachers)
class TeachersTranslationOptions(TranslationOptions):
    fields = ('position', 'about')
