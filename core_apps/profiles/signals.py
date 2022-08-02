import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from auth_api.settings.base import AUTH_USER_MODEL

from core_apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"Profile created for {instance.username}")

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_profile_for_user(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"Profile saved for {instance.username}")