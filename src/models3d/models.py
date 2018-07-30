from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Model(models.Model):
    name = models.CharField(max_length=48)
    file = models.FileField(upload_to='uploads/', max_length=256)
    user = models.ForeignKey(User, related_name='models')
    vertice_count = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    nb_viewer = models.IntegerField(default=0)

    def add_viewer(self):
        """
        add a viewer
        """
        self.nb_viewer += 1
        self.save()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        super(Model, self).save(force_insert, force_update, using, update_fields)
        if self.nb_viewer == settings.NB_VIEWER_FOR_STAR:  # we can do that by signal
            from badges.models import Star
            Star.objects.get_or_create(user=self.user, model=self)

    class Meta:
        app_label = 'models3d'
