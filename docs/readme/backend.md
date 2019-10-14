Don't modify `backend.plugins.default` unless you do that in djangocms-template project - if you want to customize one of them copy-past it into another module, eg `backend.plugins.plugin_name`.

The settings.py file is split into 4 categories, keep them in mind:
- django core
- django packages
- django-cms core
- django-cms packages
