djangocms-template project is usable by itself. You can follow the local setup instructions to try it out.


Divio Integration Setup
-------------------------------------------------------------------------------
- create a new project on divio of the type python3, django, select custom repository and add your own - ⚠️ DO NOT DEPLOY THE TEST SERVER as this migrates the db (unless you want to run into migration problems later)
- in the divio addons install the addons: django-cms and django-filer 
- add another remote: `git remote add template git@gitlab.com:what-digital/djangocms-template.git` and `git fetch template -a`
- merge in djangocms-template/divio - `git pull template divio --allow-unrelated-histories` - once you merge you're going to get some merge conflicts: resolve them by accepting both versions 
- compile the requirements - see the instructions below
- remove only `pip-reqs compile` command from reqs install - everything else leave as it is
- in the Development Setup below replace `create an .aldryn file` with the content as `{"id": {project_id}, "slug": "{project_slug}"}`, the ID can be found in the dashboard url - `https://control.divio.com/control/{org_id}/edit/{project_id}/`, the slug is on that page as well
- remove this section from README.md, along with the first sentence about djangocms-template independent setup. Also remove the `docs` directory - it should be stored only within this the source repository.

If you DID deploy the test server before merging in djangocms-template and you run into migration errors:

- migrate the local db and then push it to the divio test server: `divio project push db`
- deploy the test server on divio.com


Development Setup
-------------------------------------------------------------------------------
Built on Python 3.6, Django 2.2, DjangoCMS 3.7, Webpack 4, TypeScript 3.

- create an `.aldryn` file, it should look as `{"id": {project_id}, "slug": "{project_slug}"}`
- for the rest see the general [setup instructions](https://gitlab.com/what-digital/wiki/-/blob/master/info/projects/djangocms-template/setup-instruction.md)

Guidelines:
- [backend](https://gitlab.com/what-digital/djangocms-template/-/blob/master/docs/readme/backend.md)
- [frontend](https://gitlab.com/what-digital/djangocms-template/-/blob/master/docs/readme/frontend.md)
