from django.db import models
from django.utils.translation import ugettext_lazy as _


class StandardMetadata(models.Model):
    """
    A basic (abstract) model for metadata.
    """
    created = models.DateTimeField(_('Created'), auto_now=True)
    updated = models.DateTimeField(_('Updated'), auto_now_add=True)
    is_deleted = models.BooleanField(_('Is deleted'), default=False, db_index=True)

    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.save()


class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(is_deleted=False)
