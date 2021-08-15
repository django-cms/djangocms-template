Store project-related applications in a project module, eg `backend.{project_name}`. The root `backend` module reserve for global non-project related apps from the template, eg `backend.auth` or `backend.site_config`.

The settings.py and requirements.in files are split into categories and have comments, adhere to that.

The `backend/templates` directory is only for global templates, for anything else use app specific templates per django guidelines.

When you need to override a plugin templates create a directory `backend.plugins.overrides.{plugin_name}`.

### envs

When you're editing the env files add the changes to another inactive changes, this way you're never going to commit those changes to git.

![](/docs/guidelines/img/changset.png)
