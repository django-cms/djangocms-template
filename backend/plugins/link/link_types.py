from djangocms_blog.models import Post
from linkit.types.model import ModelLinkType


class PatchedModelLinkType(ModelLinkType):
    def real_value(self):
        if isinstance(self.link.data('value').get('model'), int):
            return self.model.objects.filter(pk=self.link.data('value').get('model')).first()
        else:
            return self.model.objects.filter(pk=self.link.data('value').get('model').pk).first()


class DjangocmsBlogPostLinkType(PatchedModelLinkType):
    identifier = 'djangocms_blog'
    type_label = 'Story'
    model = Post
