from django.db import models
from django.core.exceptions import ValidationError

from ..base.models import BaseMixinModel
# Create your models here.

class Semester(BaseMixinModel):
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
    academic_year=models.ForeignKey(to="AcademicYear", on_delete=models.CASCADE, 
                                    null=True, blank=True, related_name="semester")

class AcademicYear(BaseMixinModel):
    name=models.CharField(max_length=255, null=True, blank=True)
    description=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

def validate_range_of_class(value):
    if value < 1 or value > 11:
        raise ValidationError(f'Value {value} must be between 1 and 11 (inclusive).')

class ClassOfBranch(BaseMixinModel):
    class Language(models.TextChoices):
        ENGLISH = "english", "english"
        RUSSAIN = "russian", "russian"
        UZBEK = "uzbek", "uzbek"
    
    class ClassStatus(models.TextChoices):
        NEW = "new", "new"
        STARTED = "started", "started"
        FINISHED = "finished", "finished"

    class GradeOptions(models.TextChoices):
        A="A","A"
        B="B","B"
        C="C","C"
        D="D","D"
        E="E","E"
        F="F","F"

    branch=models.ForeignKey(to="branch.Branch", on_delete=models.SET_NULL, null=True, blank=True)
    language=models.CharField(max_length=255, null=True, blank=True, choices=Language)
    academic_year=models.ForeignKey(to="AcademicYear", on_delete=models.SET_NULL, null=True, blank=True)
    grade=models.IntegerField(validators=[validate_range_of_class], null=True, blank=True)
    grade_options=models.CharField(max_length=100, choices=GradeOptions, null=True, blank=True)
    teacher=models.ForeignKey(to="employee.Employee", on_delete=models.CASCADE, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    status=models.CharField(max_length=255, null=True, blank=True, choices=ClassStatus)

    def __str__(self):
        return f"{self.grade}-{self.grade_options}"

class Subject(BaseMixinModel):
    duration=models.BooleanField(null=True, blank=True, default=False)
    teacher=models.ForeignKey("employee.Employee", on_delete=models.CASCADE, null=True, blank=True)

class FolderOfDocuments(BaseMixinModel):
    name=models.CharField(max_length=255, null=True, blank=True)
    academic_year=models.ForeignKey(to="AcademicYear", on_delete=models.SET_NULL, null=True, blank=True)

class DocumentsAcademicYear(BaseMixinModel):
    academic_year=models.ForeignKey(to="AcademicYear", on_delete=models.CASCADE, 
                                    null=True, blank=True,related_name="documents")
    file=models.FileField(upload_to=f"documents/")

class Event(BaseMixinModel):
    academic_year=models.ForeignKey(to="AcademicYear", on_delete=models.SET_NULL, null=True, blank=True)
    