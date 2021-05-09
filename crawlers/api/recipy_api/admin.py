from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models

admin.site.site_header = _('Recipy Admin')
admin.site.site_title = _('Recipy Admin')
