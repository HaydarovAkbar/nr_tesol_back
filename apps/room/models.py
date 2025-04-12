from django.db import models
from ..base.models import BaseMixinModel

class Room(BaseMixinModel):
    branch=models.ForeignKey(to="branch.Branch", on_delete=models.SET_NULL, null=True, blank=True)
    room_numer=models.IntegerField(blank=True, null=True)
    floor=models.IntegerField(null=True, blank=True)
    description=models.CharField(max_length=400, null=True, blank=True)

    