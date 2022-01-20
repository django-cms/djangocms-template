# Project setup

- `docker compose up --build -d`
- `docker compose exec python web manage.py migrate`

For setting up the database from the stage/live server see the last section about divio-cli.

### Frontend

- the frontend is starting up automagically in hot reload modus. This means you can change SCSS and the content in your browser will update instantly.
- If you want to keep an eye on the console output you can run the frontend separately in a terminal like `docker compose up frontend`
- You can also run the frontend on your host system if you happen to have node / yarn installed. Open a terminal, cd into the frontend folder and run `yarn serve` 
- For debugging you can see a webpack dev server asset report here: http://0.0.0.0:8090/webpack-dev-server

### Update requirements.txt

`docker-compose run --rm web bash -c "cd backend && pip-compile requirements.in > requirements.txt"`

For installing the compiled requirements in docker you have to rebuild it with `docker-compose build`.

### Pulling the external database and media

- `cp .divio/config-example.json .divio/config.json`
- run `pip install divio-cli` & `divio login` outside of docker
- run `divio project pull db test` and `divio project pull media test` outside of docker

## Local setup without Docker 

This setup is useful when execution performance is important and you don't want to use Docker for the backend and frontend, only for DB.
Using of virtualenv (and other [tools](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)) is very useful here, you might want to run something like this to prepare your local environment:

- `mkvirtualenv myproject`
- `pip install -r backend/requirements.txt`

1. Start DB via docker-compose: `docker-compose up db` 
2. Enable reading local env file to **settings.py**: `environ.Env.read_env(os.path.join(BASE_DIR, '.local-env'))` 
3. Run the backend: `python manage.py runserver`
4. Run the frontend: 
   1. `cd frontend`
   2. `yarn start`

## Recommendations

Don't hesitate to address divio support, a significant amount of features might not work according to the docs, or there are no docs. We're also keeping an open github repository for keeping track of our past issues with divio deployments - https://github.com/what-digital/divio/issues

### Shell
- `docker-compose run --rm web bash` - a disposable container

### How to drop the database
You can flush the local & server db in the following way:
- docker-compose rm db
- run migrations - now you have an empty db
- push it to the server `divio project push db test`

### How to edit an external package in docker
- Firstly the files that pycharm/intellij shows you in the docker remote files are editable but have no effect - it's just a copy-past of the real files
- See the divio guide - https://docs.divio.com/en/latest/how-to/create-addon.html


### Simulating the live environment locally

Sometimes nasty errors only show up on production environments. Here is how you can simulate a production environment locally to catch those nasty ones.

1. Add and set some env vars in `.env-local` 

```
DEBUG=False
STAGE=live
DEBUG_PROPAGATE_EXCEPTIONS = True
SSO_DSN=https://user:pass@control.divio.com/auth/  # ssh into the liveserver and printenv for this info
DOMAIN=djangocms-template.0.0.0.0.nip.io
```
2. Run `docker-compose run frontend yarn build`
3. Then run `./manage.py collectstatic --ignore node_modules`
4. and then rerun `docker-compose up web -d`
