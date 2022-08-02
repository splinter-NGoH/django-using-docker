from django.db import models
import uuid


class TimeStampUUIDModel(models.Model):
    """
    Abstract base class model that provides self-updating ``created`` and ``modified`` fields.
    """
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', "-updated_at"]