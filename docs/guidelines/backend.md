Don't modify `backend.plugins.default` unless you do that in djangocms-template project - if you want to customize one of them copy-past it into another module under the `plugins` directory, eg `backend.plugins.plugin_name`.

Store project-related applications in a project module, eg `backend.dectris`. The root `backend` module reserve for non-project related apps, eg `auth` or `articles`.

The settings.py file is split into 4 categories, keep them in mind:
- django core
- django packages
- django-cms core
- django-cms packages

The `backend/templates` directory is only for global templates, for anything else use app specific templates per django guidelines.

### envs

When you're editing the env files add the changes to another inactive changes, this way you're never going to commit those changes to git.

![](/info/projects/djangocms-template/guidelines/img/changset.png)
