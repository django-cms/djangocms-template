Divio Project Setup
-------------------------------------------------------------------------------

- create a new project on divio without deploying it, set the type python3, django with default boilerplate
- create a new empty repository on git and add the following remotes:
    - `git remote add template git@gitlab.com:what-digital/djangocms-template.git`
    - `git remote add divio git@git.divio.com:{project-slug}.git`, replace `{project-slug}`, the project slug can be found in the project title and url:
        <details>

      ![](/docs/guidelines/img/project-slug.png)

        </details>
- run `git pull template master`
- run `git push --force divio master`
- make sure that your project and divio repositories are in sync, now switch divio to gitlab external repository according to [divio docs](https://docs.divio.com/en/latest/how-to/resources-configure-git/)
- set up a gitlab webhook
- compile the requirements (see the [setup instructions](/docs/local-setup-instructions.md))
- update the `.divio/config-example.json` file with the values from your project, in order to find your slug and id run a divio-cli command `divio project list -g`
- to test and live server add a new env variable - `DJANGO_SETTINGS_MODULE`=`backend.settings`
- in the main README.md remove everything and replace it with the `README.md template` section from below (don't forgot to update the urls in it). Also go through the following steps:
    - remove the `docs` directory - it should be stored only within this source repository
    - remove `base.Dockerfile` and `LICENSE` files
    - if you're planning to use only one CMS language, you can go to [frontend/global/ts/ckeditor-config.js](/frontend/global/ts/ckeditor-config.js) and update the SCAYT line to `scayt_autoStartup = true`
- deploy the stage server

⚠ ️BEWARE: If you get a migration error on Divio deployment, follow the instructions for database reset placed in [setup instructions](https://gitlab.com/what-digital/djangocms-template/-/blob/3.0.0.0/docs/setup-instruction.md#how-to-drop-the-database)

For what.digital specific final steps see [the respective nuclino file](https://share.nuclino.com/p/djangocms-template-setup-steps-yzx_82bXA8b8YX_2xG2ccF).


README.md template
-------------------------------------------------------------------------------

You can access the stage server without logging in through the url https://{domain}.aldryn.io/?anonymous-access=true

### Development Setup

Built on Python 3.9, Django 3.1, DjangoCMS 3.8, Webpack 5, TypeScript 4.

See the general [setup instructions](https://gitlab.com/what-digital/djangocms-template/-/blob/3.0.0.0/docs/setup-instruction.md)

[Project intro & guidelines](https://gitlab.com/what-digital/djangocms-template/-/blob/3.0.0.0/README.md)
