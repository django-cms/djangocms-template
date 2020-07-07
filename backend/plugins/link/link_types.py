from djangocms_blog.models import Post
from linkit.types.model import ModelLinkType


class DjangocmsBlogPostLinkType(ModelLinkType):
    identifier = 'djangocms_blog'
    type_label = 'Story'
    model = Post
