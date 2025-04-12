from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ..base.models import BaseMixinModel

# Student Model
class Student(BaseMixinModel):
    class DocumentType(models.TextChoices):
        ID = "id", "ID"
        PASSPORT = "passport", "Passport"
        BIRTH_CERT = "birth_cert", "Birth Certificate"

    class StudentStatus(models.TextChoices):
        NEW="new","new"
        ACTIVE="active","aactive"
        INACTIVE="inactive","inactive"

    status=models.CharField(
        max_length=255, 
        choices=StudentStatus, 
        null=True, 
        blank=True
    )

    user = models.OneToOneField(
        to="account.CustomUser", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="student_profile"
    )
    document_type = models.CharField(
        max_length=20, 
        choices=DocumentType.choices, 
        null=True, 
        blank=True
    )
    passport = models.OneToOneField(
        to="Passport", 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        related_name="student"
    )
    branch=models.ForeignKey(
        to="branch.Branch", 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="student"
    )

    grade=models.ForeignKey(
        to="academic_year.ClassOfBranch",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="student"
    )
    

    def __str__(self):
        return f"Student Profile: {self.user.username}"


# Passport Model
class Passport(BaseMixinModel):
    country = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )
    act_number = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )
    document_number = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )
    document_issue_date = models.DateField(
        null=True, 
        blank=True
    )
    place_of_registration = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
    )
    is_id = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"Passport: {self.document_number}"


# Parent of Student Model
class ParentOfStudent(BaseMixinModel):
    class ParentalStatus(models.TextChoices):
        FATHER = "father", "Father"
        MOTHER = "mother", "Mother"

    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    middle_name = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )
    date_of_birth = models.DateField(
        null=True, 
        blank=True
    )
    phone_number = PhoneNumberField(
        region="UZ", 
        unique=True
    )
    email = models.EmailField(
        null=True, 
        blank=True
    )
    image = models.ImageField(
        upload_to="parents/", 
        null=True, 
        blank=True
    )
    note = models.TextField(
        null=True, 
        blank=True
    )
    parental_status = models.CharField(
        max_length=20, 
        choices=ParentalStatus.choices, 
        null=True, 
        blank=True
    )
    student = models.ForeignKey(
        to="Student", 
        on_delete=models.CASCADE, 
        related_name="parents"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Education Model
class Education(BaseMixinModel):
    class Language(models.TextChoices):
        EN = "en", "English"
        RU = "ru", "Russian"
        UZ = "uz", "Uzbek"

    language = models.CharField(
        max_length=10, 
        choices=Language.choices, 
        null=True, 
        blank=True
    )
    additional_info = models.TextField(
        null=True,
        blank=True
        )
    level = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
    )
    student = models.ForeignKey(
        to="Student", 
        on_delete=models.CASCADE, 
        related_name="education"
    )

    def __str__(self):
        return f"Education: {self.level} ({self.language})"


# Attachments Model
class Attachments(BaseMixinModel):
    student = models.ForeignKey(
        to="Student", 
        on_delete=models.CASCADE, 
        related_name="attachments"
    )
    file = models.FileField(
        upload_to="attachments/student/", 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f"Attachment for {self.student}"