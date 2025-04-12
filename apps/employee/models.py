from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ..base.models import BaseMixinModel
# Create your models here.


class PassportOfEmployee(BaseMixinModel):
    country=models.CharField(max_length=255, null=True, blank=True)
    document_number= models.CharField(max_length=255, null=True, blank=True)
    issue_date=models.DateField(null=True, blank=True)
    expiry_date=models.DateField(null=True, blank=True)
    is_id=models.BooleanField(default=False, null=True, blank=True)

class EducationOfEmployee(BaseMixinModel):

    class Status(models.TextChoices):
        HIGH="high","high"
        MIDDLE="middle","middle"
    
    name_institution=models.CharField(max_length=255, null=True, blank=True)
    specialization=models.CharField(max_length=255, null=True, blank=True)
    document_series=models.CharField(max_length=255, null=True, blank=True)
    graduation_date=models.DateField(null=True, blank=True)
    language_skill=models.CharField(max_length=255, null=True, blank=True)
    # employee=models.ForeignKey(to="Employee", on_delete=models.SET_NULL, null=True, blank=True, related_name="education")

class Attachments(BaseMixinModel):
    file=models.FileField(upload_to="employee/files/", null=True, blank=True)
    employee=models.ForeignKey(to="Employee", on_delete=models.CASCADE, null=True, blank=True, related_name="attachments")

    def __str__(self):
        return f"{self.created_at}"
    
class EmployementHistory(BaseMixinModel):

    class EmployementType(models.TextChoices):
        FUll_TIME="full_time","Full Time"
        PART_TIME="part_time","Part Time"
        HYBRID="hybrid","Hybrid"


    employee=models.ForeignKey(to="Employee", on_delete=models.SET_NULL, null=True, blank=True, related_name="employement_history")
    beginning_time=models.DateField(null=True, blank=True)
    end_time=models.DateField(null=True, blank=True)
    still_working=models.BooleanField(default=False, null=True, blank=True)
    specialization=models.CharField(max_length=255, blank=True, null=True)
    job_description=models.CharField(max_length=500, null=True, blank=True)
    organization=models.CharField(max_length=255, null=True, blank=True)
    employment=models.CharField(max_length=30, choices=EmployementType, null=True, blank=True)
    location=models.CharField(max_length=255, null=True, blank=True)


class Employee(BaseMixinModel):

    class MaritalStatus(models.TextChoices):
        SINGLE = "single", "single"
        MARRIED = "married", "married"
        WIDOWED = "widowed", "widowed"
        DIVORCED = "divorced", "divorced"
        SEPERATED = "separated", "separated"
    
    class WorkPosition(models.TextChoices):
        TEACHER="teacher","teacher"
        DIRECTOR="director","director"
        HR="hr", "hr"
        ADMISSION="admission", "admission"
        CORD_TEACHER="cord_teacher","cord_teacher"
        CHIEF="chief","chief"
        DOCTOR="doctor", "doctor"

    class EmployeeStatus(models.TextChoices):
        NEW="new","new"
        ACTIVE="active","active"
        INACTIVE="inactive","inactive"

    user=models.OneToOneField(to="account.CustomUser", 
                              on_delete=models.CASCADE, 
                              null=True, 
                              blank=True,
                              db_index=True, 
                              related_name="employee")
    
    marital_status=models.CharField(max_length=255, choices=MaritalStatus, null=True, blank=True)
    work_position=models.CharField(max_length=255, choices=WorkPosition, null=True, blank=True)
    status=models.CharField(max_length=255, choices=EmployeeStatus, null=True, blank=True)
    passport=models.OneToOneField(to="PassportOfEmployee", on_delete=models.SET_NULL, null=True, blank=True)
    branch=models.ForeignKey(to="branch.Branch", on_delete=models.SET_NULL, null=True, blank=True)
    hire_date=models.DateField(null=True, blank=True)
    description=models.CharField(max_length=400, null=True, blank=True)
    
