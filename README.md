djangocms-template project is usable by itself. You can follow the local setup instructions to try it out.


Divio Integration Setup
-------------------------------------------------------------------------------
- create a new project on divio of the type python3, django, select custom repository and add your own
- in the divio addons install the addons: django-cms and django-filer 
- add another remote: `git remote add template git@gitlab.com:what-digital/djangocms-template.git` and `git fetch template -a`
- merge in djangocms-template/divio - `git pull template divio --allow-unrelated-histories` - once you merge you're going to get some merge conflicts: resolve them by accepting both versions 
- compile the requirements (see the [setup instructions](/docs/setup-instruction.md))
- update .aldryn-example file the values from the control page eg `https://control.divio.com/control/6215/edit/81016/` the id is `81016` and the slug is can be found in the project title:
    <details>

    ![](/docs/guidelines/img/project-slug.png)

    </details>
- remove the following files and contnet:
    - remove this section from README.md, along with the first sentence about djangocms-template independent setup
    - remove the `docs` directory - it should be stored only within this source repository
    - remove base.Dockerfile and .gitlab-ci.yml


Development Setup
-------------------------------------------------------------------------------
Built on Python 3.6, Django 2.2, DjangoCMS 3.7, Webpack 4, TypeScript 3.

See the general [setup instructions](https://gitlab.com/what-digital/djangocms-template/-/blob/divio/docs/setup-instruction.md)

[Project intro & guidelines](https://gitlab.com/what-digital/djangocms-template/-/blob/divio/docs/README.md)
