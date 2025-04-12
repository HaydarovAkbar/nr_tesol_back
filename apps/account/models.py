from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from ..base.models import BaseMixinModel


# Create your models here.
class CustomUser(AbstractUser, BaseMixinModel):
    class GenderStatus(models.TextChoices):
        MALE = "male", "male"
        FEMALE = "female", "female"

    middle_name=models.CharField(max_length=255, 
                                 null=True, 
                                 blank=True, 
                                 db_index=True)
    
    phone_number = PhoneNumberField(region="UZ", unique=True)

    image=models.ImageField(upload_to='media/user/',
                            blank=True, null=True,
                            verbose_name=_("Фото профиля"))
    gender=models.CharField(max_length=255, choices=GenderStatus, null=True, blank=True)

    date_of_birth=models.DateField(null=True, blank=True)
    address=models.CharField(max_length=400, null=True, blank=True)
    region=models.CharField(max_length=255, null=True, blank=True)
    city=models.CharField(max_length=255, null=True, blank=True)
    is_student=models.BooleanField(null=True, blank=True, default=False)
    is_employee=models.BooleanField(null=True, blank=True, default=False)
    password1=models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = now()

        super(CustomUser, self).save(*args, **kwargs)
        return self
    
    def __str__(self):
        return self.username
    
    def get_image_url(self):
        return self.image.url


