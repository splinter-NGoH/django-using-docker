from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from core_apps.common.models import TimeStampUUIDModel

User = get_user_model()


class Rating(TimeStampUUIDModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("poor")
        RATING_2 = 2, _("fair")
        RATING_3 = 3, _("good")
        RATING_4 = 4, _("very good")
        RATING_5 = 5, _("excellent")

    article = models.ForeignKey(
        "articles.Article", on_delete=models.CASCADE, related_name="article_rating"
    )
    rated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_who_rated",
    )
    value = models.IntegerField(
        verbose_name=_("value"),
        choices=Range.choices,
        default=0,
        help_text="1=Poor, 2=fair, 3=good, 4=very good 5",
    )
    reiview = models.TextField(verbose_name=_("rating review"), blank=True)

    class Meta:
        unique_togetjer = ["rated_by", "article"]

        def __str__(self):
            return f"{self.article.title} rated at {self.value}"
