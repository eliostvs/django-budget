from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import ActiveManager, StandardMetadata


class Category(StandardMetadata):
    """
    Categories are the means to loosely tie together the transactions and
    estimates.

    They are used to aggregate transactions together and compare them to the
    appropriate budget estimate. For the reasoning behind this, the docstring
    on the Transaction object explains this.
    """
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'), unique=True)

    objects = models.Manager()
    active = ActiveManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category:category_edit', args=[self.slug])

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
