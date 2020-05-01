Project setup
-------------------------------------------------------------------------------

#### Pure docker (easy, slow)

This setup is highly convenient and simple, but shouldn't be used for long-term development, since docker isn't suitable for debugging, significantly degrades performance, has immature and unstable IDEA integrations, etc. But it's perfect for quick setup or people who don't want to configure python or nodejs.

- docker-compose build
- docker-compose run --rm web fish --command 'python manage.py migrate'
- docker-compose up

For setting up the database from the stage/live server see the last section about divio-cli.

#### Docker backend and native frontend

Perfect for people who aren't planning to do any backend development and want the real-time webpack rebuilds.

- remove `IS_RUN_FRONTEND_IN_DOCKER=true` from `.env-local` file  
- `docker-compose build`
- `docker-compose run --rm web fish --command 'python manage.py migrate'`
- install yarn and node 10 outside of docker
- `yarn install --pure-lockfile`
- `yarn start`
- `docker-compose up web`

#### Native setup

The most efficient and reliable setup for backend development.

- `pip install -r requirements.txt`
- add a new line - `127.0.0.1 postgres` - to your system `/etc/hosts` file
- `docker-compose up db`
- `python manage.py migrate`
- `python manage.py runserver`
- install yarn and node 10
- `yarn install --pure-lockfile`
- `yarn start`

### Update requirements.txt

`docker-compose run --rm web fish --command 'pip-reqs compile; pip-reqs resolve'`

For installing the compiled requirements in docker you have to rebuild it with `docker-compose build`.

### Cloning external database and media

- copy `.aldryn-example` as `.aldryn` file
- run `pip install divio-cli` outside of docker
- run `divio project pull db test` and `divio project pull media test` outside of docker

Advices
-------------------------------------------------------------------------------

### Shell
- `docker-compose run --rm web fish` - a disposable container

### How to drop the database
You can flush the local & server db in the following way:
- docker-compose rm db
- run migrations - now you have an empty db
- push it to the server `divio project push db test`

### How to edit an external package in docker
- Firstly the files that pycharm/intellij shows you in the docker remote files are editable but have no effect - it's just a copy-past of the real files
- See the divio guide - https://docs.divio.com/en/latest/how-to/create-addon.html

### base.Dockerfile rebuilding

It's used in docker files as `FROM registry.gitlab.com/what-digital/djangocms-template:latest`. If you want to modify it and push another version:

- `docker login registry.gitlab.com`
    - gitlab will ask for a password - this is a bug, it's actually asking for an access token that must be created [in your profile](https://gitlab.com/profile/personal_access_tokens)
- `docker build -t registry.gitlab.com/what-digital/djangocms-template -f base.Dockerfile .`
- `docker tag registry.gitlab.com/what-digital/djangocms-template:latest registry.gitlab.com/what-digital/djangocms-template:{version}`, replace `{version}`, see [versioning documentation](https://gitlab.com/what-digital/tech-docs/-/blob/master/coding-guidelines/translations.md)
- `docker push registry.gitlab.com/what-digital/djangocms-template`
