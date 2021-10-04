Divio Project Setup
-------------------------------------------------------------------------------

- create a copy of the https://github.com/django-cms/djangocms-template (copy it locally to your own repo or fork it on github)
- In control.divio.com in your account or organisation create a new project on divio (NEW PROJECT FROM GIT REPOSITORY)
- Then in Divio Control 
   1. go to services and create a postgres and a persistent storage service
   2. go to Env Vars and set `DEBUG` to `True` for the test env
   3. go to Settings and set the following Release Commands:
      - `python manage.py migrate`
      - `python manage.py clear_cache`
      - `python manage.py test_pages_on_real_db`
   4. go to Repository and set up a webhook for your repository
- update the `.divio/config-example.json` file with the values from your project, in order to find your slug and id run a divio-cli command `divio project list -g`
- in the main README.md remove everything and replace it with the `README.md template` section from below (don't forgot to update the urls in it). Also go through the following steps:
    - remove the `docs` directory - it should be stored only within this source repository
    - remove the `LICENSE` files
    - if you're planning to use only one CMS language, you can go to [frontend/global/ts/ckeditor-config.js](/frontend/global/ts/ckeditor-config.js) and update the SCAYT line to `scayt_autoStartup = true`
- deploy the test environment

⚠ ️BEWARE: If you get a migration error on Divio deployment, follow the instructions for database reset placed in [setup instructions](https://gitlab.com/what-digital/djangocms-template/-/blob/3.0/docs/local-setup-instructions.md#how-to-drop-the-database)

For what. specific final steps see [the respective nuclino file](https://share.nuclino.com/p/djangocms-template-setup-steps-yzx_82bXA8b8YX_2xG2ccF).


README.md template
-------------------------------------------------------------------------------

You can access the stage server without logging in through the url https://{domain}.aldryn.io/?anonymous-access=true

### Development Setup

Built on Python 3.9, Django 3.1, DjangoCMS 3.9, Webpack 5, TypeScript 4.

See the general [setup instructions](https://gitlab.com/what-digital/djangocms-template/-/blob/3.0/docs/local-setup-instructions.md)

[Project intro & guidelines](https://gitlab.com/what-digital/djangocms-template/-/blob/3.0/docs/README.md)
