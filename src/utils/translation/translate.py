from modeltranslation.translator import TranslationOptions, register
from ..models import About, Language, Partners


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
