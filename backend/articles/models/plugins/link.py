from cms.models.pluginmodel import CMSPlugin
from django.db import models

from backend.articles.models import Article


class ArticleLinkModel(CMSPlugin):
    # and now... magic! the "name" field is automatically assumed to be the field that will hold the selected text
    name = models.CharField(max_length=2048, blank=False)
    item = models.ForeignKey(Article, on_delete=models.PROTECT)
