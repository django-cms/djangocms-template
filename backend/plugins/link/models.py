from cms.models import CMSPlugin
from linkit.model_fields import LinkField


class LinkPluginModel(CMSPlugin):
    link = LinkField(allow_target=True, allow_no_follow=True, types=['blog', 'page', 'file', 'input'])

    def __str__(self) -> str:
        return self.link.label
