## Setup
- do a global replace of the string `project_name` on whatever you want
- rename `project_name` directory

## Admin Panel
The testing user for stage and local setup:
- test@what.digital
- test@what.digital

## Development Setup
- install yarn https://yarnpkg.com/en/docs/install
- `yarn install`
- `yarn start`
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver`

#### With Docker
- `docker-compose up web`

#### .env
- add the `.env` file in the run configuration in the `EnvFile` tab (press Cmd+Shift+. to see hidden files in the Mac OS X file dialog)


## Notes
Don't modify the default_plugins - if you want to use one copy past it into another place.


## what.digital Packages
- https://pypi.org/project/django-env-settings/
- https://pypi.org/project/django-testuser/
