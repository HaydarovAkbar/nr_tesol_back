from modeltranslation.translator import TranslationOptions, register
from ..models import News, FAQ


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
