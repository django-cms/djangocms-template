Don't modify `backend.plugins.default` unless you do that in djangocms-template project - if you want to customize one of them copy-past or move it into another module under the `plugins` directory, eg `backend.plugins.{project_name}.{plugin_name}`.

Store project-related applications in a project module, eg `backend.dectris`. The root `backend` module reserve for non-project related apps, eg `auth` or `articles`.

The settings.py, requirements.in and package.json files are split into categories and have comments, adhere to that.

The `backend/templates` directory is only for global templates, for anything else use app specific templates per django guidelines.

### envs

When you're editing the env files add the changes to another inactive changes, this way you're never going to commit those changes to git.

![](/docs/guidelines/img/changset.png)
