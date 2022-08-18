from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RefavoritesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.favorites'
    verbose_name = _("Favorites")
