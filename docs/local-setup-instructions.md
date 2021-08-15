Project setup
-------------------------------------------------------------------------------


- docker-compose up --build -d
- docker-compose exec web manage.py migrate'

For setting up the database from the stage/live server see the last section about divio-cli.

### Frontend

- the frontend is starting up automagically in hot reload modus. This means you can change SCSS and the content in your browser will update instantly.
- If you want to keep an eye on the console output you can run the frontend separately in a terminal like `docker compose up frontend`
- You can also run the frontend on your host system if you happen to have node / yarn installed. Open a terminal, cd into the frontend folder and run `yarn serve` 


### Update requirements.txt

`docker-compose run --rm web bash -c "cd backend && pip-compile requirements.in > requirements.txt"`

For installing the compiled requirements in docker you have to rebuild it with `docker-compose build`.

### Pulling the external database and media

- `cp .divio/config-example.json .divio/config.json`
- run `pip install divio-cli` & `divio login` outside of docker
- run `divio project pull db test` and `divio project pull media test` outside of docker


Recommendations
-------------------------------------------------------------------------------

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
