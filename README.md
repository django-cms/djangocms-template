Development Setup
-------------------------------------------------------------------------------
Built on Python 3.6, Django 2.1, DjangoCMS 3.7, Webpack 4, TypeScript 3.

- remove djangocms-text-ckeditor from installed addons through the divio dashboard
- add your `INSTALLED_ADDONS` to `requirements.in`
- add your project ID and slug to `.aldryn`
    - the ID can be found in the dashboard url - `https://control.divio.com/control/{org_id}/edit/{project_id}/`
- `docker-compose build`
- `pip install divio-cli`
- `divio project pull db test`
- install yarn and node 10 outside of docker
- `yarn install --pure-lockfile`
- `yarn start`

Testing:
- `docker-compose exec web fish --command 'python manage.py test --keepdb'`

Requirements update:
- `docker-compose exec web fish --command 'pip-reqs compile'`

Shell:
- `docker-compose exec web fish`


Development Guidelines
-------------------------------------------------------------------------------
This project is a fork of [djangocms-template](https://gitlab.com/what-digital/djangocms-template/), if you would like to edit the basic structure - create an MR there.

- [backend guidelines](/docs/readme/backend.md)
- [frontend guidelines](/docs/readme/frontend.md)
