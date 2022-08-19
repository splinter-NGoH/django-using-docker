from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RatingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.rating"
    verbose_name = _("Rating")
