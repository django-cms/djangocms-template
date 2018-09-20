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


