djangocms-template project is usable by itself. You can follow the local setup instructions to try it out.


Divio Integration Setup
-------------------------------------------------------------------------------
- create a new project on divio of the type python3, django with default boilerplate
    - in the divio addons install the addons: aldryn-django-cms and django-filer
- clone this repository and add remotes
    - `git remote add origin git@gitlab.com:what-digital/{your-project}.git`, replace `{your-project}`
    - `git remote add template git@gitlab.com:what-digital/djangocms-template.git`
    - `git remote add divio git@git.divio.com:{project-slug}.git`, replace `{project-slug}`
- merge in divio repository - `git pull divio master --allow-unrelated-histories` - once you merge you're going to get some merge conflicts: resolve them by prioritizing the template version
- compile the requirements (see the [setup instructions](/docs/setup-instruction.md))
- make sure that your project and divio repositories are in sync, now switch divio to gitlab external repository
- set up a gitlab webhook
- update .aldryn-example file with the values from the control page eg `https://control.divio.com/control/6215/edit/81016/` the id is `81016` and the slug is can be found in the project title:
    <details>

    ![](/docs/guidelines/img/project-slug.png)

    </details>
- remove the following files and contnet:
    - remove this section from README.md, along with the first sentence about djangocms-template independent setup
    - remove the `docs` directory - it should be stored only within this source repository
    - remove base.Dockerfile and .gitlab-ci.yml
- deploy the stage server


Development Setup
-------------------------------------------------------------------------------
Built on Python 3.6, Django 2.2, DjangoCMS 3.7, Webpack 4, TypeScript 3.

See the general [setup instructions](https://gitlab.com/what-digital/djangocms-template/-/blob/master/docs/setup-instruction.md)

[Project intro & guidelines](https://gitlab.com/what-digital/djangocms-template/-/blob/master/docs/README.md)
