from django.apps import AppConfig


class LinkAppConfig(AppConfig):
    name = 'backend.plugins.link'

    def ready(self):
        from backend.plugins.link.link_types import DjangocmsBlogPostLinkType
        from linkit.types import type_manager as linkit_manager
        linkit_manager.register(DjangocmsBlogPostLinkType)
