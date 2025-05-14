from modeltranslation.translator import TranslationOptions, register
from ..models import News, About


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
