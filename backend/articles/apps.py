from django.apps import AppConfig


class ArticlesApp(AppConfig):
    name = 'backend.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import backend.articles.signals
