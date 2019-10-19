Development Setup
-------------------------------------------------------------------------------
Built on Python 3.6, Django 2.1, DjangoCMS 3.7, Webpack 4, TypeScript 3.

- add your project ID and slug to `.aldryn`
    - the ID can be found in the dashboard url - `https://control.divio.com/control/{org_id}/edit/{project_id}/`
- `docker-compose build`
- `pip install divio-cli`
- `divio project pull db test`
- `./manage.py runserver`
- install yarn and node 10
- `yarn install --pure-lockfile`
- `yarn start`

Testing:
- `./manage.py collectstatic`
- `./manage.py test --keepdb`

#### Docker Setup
- `docker-compose build`
- `docker-compose up`
- install yarn and node 10
- `yarn install --pure-lockfile`
- `yarn start`


Development Guidelines
-------------------------------------------------------------------------------
This project is a fork of [djangocms-template](https://gitlab.com/what-digital/djangocms-template/), if you would like to edit the basic structure - create an MR there.

- [backend guidelines](/docs/readme/backend.md)
- [frontend guidelines](/docs/readme/frontend.md)
