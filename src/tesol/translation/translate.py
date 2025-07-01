from modeltranslation.translator import TranslationOptions, register
from ..models import About, News, Partners, CourseType, Courses, Teachers, Accreditation, Services


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(CourseType)
class CourseTypeTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Teachers)
class TeachersTranslationOptions(TranslationOptions):
    fields = ('position', 'about')


@register(Accreditation)
class AccreditationTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')