from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class LanguageModel(models.Model):
    Language = models.CharField(_("Language"), max_length=255)
    Code = models.CharField(_("Code"), max_length=15)
    def __str__(self):
        return self.Language

