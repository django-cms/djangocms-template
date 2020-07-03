djangocms-template project is usable by itself. You can follow the local setup instructions to try it out.


Divio Integration Setup
-------------------------------------------------------------------------------
- create a new project on divio without deploying it, set the type python3, django with default boilerplate
- create a new empty repository on git and add the following remotes:
    - `git remote add template git@gitlab.com:what-digital/djangocms-template.git`
    - `git remote add divio git@git.divio.com:{project-slug}.git`, replace `{project-slug}`
- run `git pull template master`
- run `git push --force divio master`
- make sure that your project and divio repositories are in sync, now switch divio to gitlab external repository according to [divio docs](https://docs.divio.com/en/latest/how-to/resources-configure-git/)
- set up a gitlab webhook
- compile the requirements (see the [setup instructions](/docs/setup-instruction.md))
- update .aldryn-example file with the values from the control page eg `https://control.divio.com/control/6215/edit/81016/` the id is `81016` and the slug is can be found in the project title:
    <details>

    ![](/docs/guidelines/img/project-slug.png)

    </details>
- remove the following files and content:
    - remove this section from README.md, along with the first sentence about djangocms-template independent setup
    - remove the `docs` directory - it should be stored only within this source repository
    - remove base.Dockerfile and .gitlab-ci.yml
- deploy the stage server
 
⚠ ️BEWARE: If you get a migration error on Divio deployment, follow the instructions for database reset placed in [setup instructions](https://gitlab.com/what-digital/djangocms-template/-/blob/master/docs/setup-instruction.md#how-to-drop-the-database)

### Mailtrap setup

- signup with a tech eamil, eg `tech+{project}@what.digital` https://mailtrap.io/register/signup
- save the login/password to the project's 1password vault
- add `EMAIL_URL` to the divio envs `smtps://{username}:{password}@smtp.mailtrap.io:2525`

### Sentry setup

- create a new account using tech email `tech+{project}@what.digital`
- save the login/password to the project's 1password vault
- add `SENTRY_DSN` to the divio envs

Development Setup
-------------------------------------------------------------------------------
Built on Python 3.6, Django 2.2, DjangoCMS 3.7, Webpack 4, TypeScript 3.

See the general [setup instructions](https://gitlab.com/what-digital/djangocms-template/-/blob/master/docs/setup-instruction.md)

[Project intro & guidelines](https://gitlab.com/what-digital/djangocms-template/-/blob/master/docs/README.md)
