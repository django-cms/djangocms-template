Divio Integration Setup
-------------------------------------------------------------------------------
- remove djangocms-text-ckeditor from installed addons through the divio dashboard - only in the dashboard, it will be installed through requirements.in later
- add your `INSTALLED_ADDONS` to `requirements.in` by merging in djangocms-template/divio - `git pull template divio --allow-unrelated-histories` - once you merge you're going to get a merge conflict in `requirements.in`, resolve it by accepting both versions 
- compile the requirements - see the instructions below
- remove only `pip-reqs compile` command from reqs install - everything else leave as it is
- remove this section from README.md


Development Setup
-------------------------------------------------------------------------------
Built on Python 3.6, Django 2.1, DjangoCMS 3.7, Webpack 4, TypeScript 3.

- create an `.aldryn` file, it's should look as `{"id": {project_id}, "slug": "{project_slug}"}` the ID can be found in the dashboard url - `https://control.divio.com/control/{org_id}/edit/{project_id}/`, the slug is on that page as well
- `docker-compose build`
- run `pip install divio-cli` outside of docker
- run `divio project pull db test` and `divio project pull media test` outside of docker, or `docker-compose exec web fish --command 'python manage.py migrate'`
- install yarn and node 10 outside of docker
- `yarn install --pure-lockfile`
- `yarn start`
- `docker-compose up`

Translations generation:
- `django-admin makemessages -l {lang_code} --no-wrap`

Testing:
- `docker-compose exec web fish --command 'python manage.py test --keepdb'`

Compile requirements.txt from requirements.in, for updating the requirements run `docker-compose build`
```bash
docker-compose run --rm web bash -c '

export PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/+simple/}
export WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/}

pip-reqs compile
pip-reqs resolve
pip install --no-index --no-deps --requirement requirements.urls
'
```

Shell:
- `docker-compose exec web fish` - a persistent container with the correct ENVs

#### How to drop the database
You can flush the local & server db in the following way:
- remove the db container along with its data volume
- run migrations - now you have an empty db
- push it to the server `divio project push db test`


Development Guidelines
-------------------------------------------------------------------------------
This project is a fork of [djangocms-template](https://gitlab.com/what-digital/djangocms-template/), if you would like to edit the basic structure - create an MR there.

- [backend guidelines](/docs/readme/backend.md)
- [frontend guidelines](/docs/readme/frontend.md)
