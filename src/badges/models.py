from django.contrib.auth.models import User
from django.db import models

from models3d.models import Model


class Star(models.Model):
    user = models.ForeignKey(User)
    model = models.ForeignKey(Model)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'model')


class Collector(models.Model):
    user = models.OneToOneField(User)


class Pioneer(models.Model):
    user = models.OneToOneField(User)
