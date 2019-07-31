## Setup
- do a global replace of the string `project_name` on whatever you want, do the same for `PROJECT_NAME`
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

#### Frontend Integration with DevTools
- open devtools and add the project folder (where manage.py is) as a workspace
    <details>
    <summary>image</summary>
    
    ![](/docs/front-int-example.png)
    
    </details>
- now you can edit the source maps and save the scss using as Ctrl+S or CMD+S - webpack is going to auto reload right away
- you can also set breaking points for debugging directly on ts files
- also the styles view is linked to the source maps
    <details>
    <summary>image</summary>
    
    ![](/docs/front-linked-styles.png)
    
    </details>

#### With Docker
- `docker-compose up web`

#### .env
- add the `.env` file in the run configuration in the `EnvFile` tab (press Cmd+Shift+. to see hidden files in the Mac OS X file dialog)


## Notes
Don't modify the default_plugins - if you want to use one copy past it into another place.


## what.digital Packages
- https://pypi.org/project/django-env-settings/
- https://pypi.org/project/django-testuser/
