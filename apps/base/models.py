from django.contrib.gis.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
# Create your models here.

# class MyModelManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_deleted=False)
    

class BaseMixinModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_("created"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated"))
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def restore(self):
        """Restore a soft-deleted object."""
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    @classmethod
    def all_objects(cls):
        """Return all objects, including soft deleted ones."""
        return cls.objects.all()

    @classmethod
    def active_objects(cls):
        """Return only active (non-deleted) objects."""
        return cls.objects.filter(is_deleted=False)
    # objects = MyModelManager()    

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.pk}>"
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = now()
        self.save()

