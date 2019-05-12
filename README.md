The default testing user for non-prod environment: test@what.digital / test@what.digital


## Docker
- There is docker support so that you dont have to set up a python virtual environment on your host
- Install docker on your machine (including docker-compose)
- Run `docker-compose up web`


## Backend Dev
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver`


## Frontend Dev
- By default, the page is blank, because all javascript and styles are deferred. In order to show content, go through
the following steps:

- `npm install`
- `npm start`
- `./manage.py runserver` or fire up the project in Pycharm (recommended)

- All the sass and js is in `private/`
- Use npm to install libraries (like jquery) instead of adding them to the source

- BEWARE: Dont add any jQuery dependend js to the templates, use the private/js folders instead to add it to webpack. The app.js bundle is loaded in deferred mode!


## Pycharm
- add the `.env` file in the run configuration in the `EnvFile` tab (press Cmd+Shift+. to see hidden files in the Mac OS X file dialog)
