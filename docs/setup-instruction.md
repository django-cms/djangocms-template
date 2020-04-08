Project setup
-------------------------------------------------------------------------------

#### Pure docker (easy, slow)

This setup is highly convenient and simple, but shouldn't be used for long-term development, since docker isn't suitable for debugging, significantly degrades performance, has immature and unstable IDEA integrations, etc. But it's perfect for quick setup or people who don't want to configure python or nodejs.

- docker-compose build
- docker-compose run --rm web bash --command 'python manage.py migrate'
- docker-compose up

For setting up the database from the stage/live server see the last section about divio-cli.

#### Docker backend and native frontend

Perfect for people who aren't planning to do any backend development and want the real-time webpack rebuilds.

- remove `IS_RUN_FRONTEND_IN_DOCKER=true` from `.env-local` file  
- `docker-compose build`
- `docker-compose run --rm web bash --command 'python manage.py migrate'`
- install yarn and node 10 outside of docker
- `yarn install --pure-lockfile`
- `yarn webpack-dev-server`
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
- `yarn webpack-dev-server`

#### Update requirements.txt

`docker-compose run --rm web fish --command 'pip-reqs compile; pip-reqs resolve'`

For installing the compiled requirements in docker you have to rebuild it with `docker-compose build`.

### Cloning external database and media

- create an `.aldryn` file, it should look as `{"id": "{project_id}", "slug": "{project_slug}"`, you can find those values on the control panel page eg `https://control.divio.com/control/6215/edit/81016/` the id is `81016` and the slug is can be found in the project title:
    <details>

    ![](/info/projects/djangocms-template/guidelines/img/project-slug.png)

    </details>
- run `pip install divio-cli` outside of docker
- run `divio project pull db test` and `divio project pull media test` outside of docker

Advices
-------------------------------------------------------------------------------

### Shell
- `docker-compose run --rm web fish` - a disposable container

### Translations
- `django-admin makemessages -l {lang_code} --no-wrap`

### How to drop the database
You can flush the local & server db in the following way:
- remove the db container along with its data volume
- run migrations - now you have an empty db
- push it to the server `divio project push db test`

### How to edit an external package in docker
- Firstly the files that pycharm/intellij shows you in the docker remote files are editable but have no effect - it's just a copy-past of the real files
- See the divio guide - https://docs.divio.com/en/latest/how-to/create-addon.html

### base.Dockerfile rebuilding

It's used in docker files as `FROM registry.gitlab.com/what-digital/djangocms-template:latest`. If you want to modify it and push another version:

- docker login registry.gitlab.com
    - here you might need to create an api key for the password
- docker build -t registry.gitlab.com/what-digital/djangocms-template -f base.Dockerfile .
- docker push registry.gitlab.com/what-digital/djangocms-template
