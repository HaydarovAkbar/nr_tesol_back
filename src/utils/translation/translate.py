from modeltranslation.translator import TranslationOptions, register
from ..models import About, Language, Partners, Testimonials, SolidFeature, DottedShape


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Testimonials)
class TestimonialsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(SolidFeature)
class SolidFeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(DottedShape)
class DottedShapeTranslationOptions(TranslationOptions):
    fields = ('title', 'content')