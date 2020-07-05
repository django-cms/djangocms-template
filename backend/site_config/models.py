from django.db import models
from parler.models import TranslatableModel
from parler.models import TranslatedFields
from solo.models import SingletonModel


class SiteConfig(SingletonModel, TranslatableModel):
    pass

    def __str__(self) -> str:
        return "Site Config"
