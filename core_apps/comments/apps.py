from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.comments'
    verbose_name = _("Comment")
