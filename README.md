Admin Panel
-------------------------------------------------------------------------------
The login/password from the [the stage]() and local setups (created by default):
- test@what.digital
- test@what.digital


Development Setup
-------------------------------------------------------------------------------
Built on Python 3.7, Django 2.1, DjangoCMS 3.7, Webpack 4, TypeScript 3.

- `pip install -r requirements.txt`
- `./manage.py migrate`
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
- install yarn and node 10 outside of docker
- `yarn install --pure-lockfile`
- `yarn start`

Requirements update:
- `docker-compose build`

Development Guidelines
-------------------------------------------------------------------------------
This project is a fork of [djangocms-template](https://gitlab.com/what-digital/djangocms-template/), if you would like to edit the basic structure - create an MR there.

- [backend guidelines](/docs/readme/backend.md)
- [frontend guidelines](/docs/readme/frontend.md)
