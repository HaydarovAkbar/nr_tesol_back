from django.contrib.gis.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField
# from ..base.models import BaseMixinModel

# Create your models here.

# class Company(models.Model):
#     class TYPE_ORGANIZATION(models.TextChoices):
#         SCHOOL="school","school"
    
#     class CompanyStatus(models.TextChoices):
#         NEW="new","new"
#         ACTIVE="active","aactive"
#         INACTIVE="inactive","inactive"

#     short_name=models.CharField(max_length=255, null=True, blank=True)
#     # type_organization=models.CharField(max_length=255,choices=TYPE_ORGANIZATION ,null=True, blank=True)
#     legal_name=models.CharField(max_length=300, null=True, blank=True)
#     stir=models.CharField(max_length=200, null=True, blank=True)
#     phone_number = PhoneNumberField(region="UZ")
#     web_site=models.URLField(null=True, blank=True)
#     email=models.EmailField(null=True, blank=True)
#     region=models.CharField(max_length=255, null=True, blank=True)
#     city=models.CharField(max_length=255, null=True, blank=True)
#     address=models.CharField(max_length=255, null=True, blank=True)
#     description=models.TextField(null=True, blank=True)
#     location=models.PointField(null=True, blank=True)
#     status=models.CharField(max_length=255, choices=CompanyStatus, null=True, blank=True)
    
#     class Meta:
#         ordering = ["city"]
#         verbose_name_plural="Companies"
    
#     def save(self, *args, **kwargs):
#         self.updated_at = now()
#         super(Company, self).save(*args, **kwargs)
#         return self
    
#     def __str__(self):
#         return f"{self.short_name}"
    

