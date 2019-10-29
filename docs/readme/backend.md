Don't modify `backend.plugins.default` unless you do that in djangocms-template project - if you want to customize one of them copy-past it into another module under the `plugins` directory, eg `backend.plugins.plugin_name`.

The settings.py file is split into 4 categories, keep them in mind:
- django core
- django packages
- django-cms core
- django-cms packages

The `backend/templates` directory is only for global templates, for anything else use app specific templates per django guidelines.
