# Local Development Setup

## Simple .env Setup

Copy `.env-local` to `.env` and add this in your virtualenv's postactivate:

```
#!/bin/bash
# This hook is sourced after this virtualenv is activated.

if [ -f ${PWD}/.env ]; then
    echo "activating .env..."
    set -a
    . ${PWD}/.env
    set +a
fi
```

### Pycharm:
- mark the `src` folder as `Sources Root` so that pycharm can find the django modules inside
- add the `.env` file in the run configuration in the `EnvFile` tab (press Cmd+Shift+. to see hidden files in the Mac OS X file dialog)


## Frontend Dev

- By default, the page is blank, because all javascript and styles are deferred. In order to show content, go through
the following steps:

- Make sure in the `.env` file you have `WEBPACK_DEV_BUNDLE_URL=http://localhost:8090/assets/bundle.js`
- `npm install`
- `npm start`
- `./manage.py runserver` or fire up the project in Pycharm (recommended)

- All the sass and js is in `private/`
- Use npm to install libraries (like jquery) instead of adding them to the source

- BEWARE: Dont add any jQuery dependend js to the templates, use the private/js folders instead to add it to webpack. The app.js bundle is loaded in deferred mode!


# Integrations

## Mapbox

Account: https://www.mapbox.com/account/

TODO: add user and pass here for the mapbox account
User:
Pass:


## Sentry

- This project has backend and frontend error monitoring at https://sentry.io/project-name/


# Custom User Model

- When adding a custom user model to djangocms and you want to run makemigrations
- this here will get in your way: https://vivazzi.pro/it/cannot-resolve-bases-for-pageuser/
- All djangocms references have to be commented out:
   - urls.py
   - settings.py INSTALLED_APPS (including any djangocms add-ons)
- comment these out, run makemigrations and then uncomment them
