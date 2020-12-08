from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (ModificationDateTimeField,CreationDateTimeField, AutoSlugField)
from datetime import datetime



class DateBaseModel(models.Model):
    """
    Base model that provides:
        * self managed created field
        * self managed modified field
    """
    created = CreationDateTimeField(_('created'))
    last_changed_date = ModificationDateTimeField(_('modified'))

    class Meta:
        get_latest_by = 'modified'
        abstract = True
