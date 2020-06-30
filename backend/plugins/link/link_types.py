from djangocms_blog.models import Post
from linkit.types.model import ModelLinkType


class PostLinkType(ModelLinkType):
    identifier = 'blog'
    type_label = 'Post'
    model = Post
