Admin Panel
-------------------------------------------------------------------------------
The login/password from the testing user on the stage and local setups (created by default):
- test@what.digital
- test@what.digital

Development Setup
-------------------------------------------------------------------------------
- install yarn https://yarnpkg.com/en/docs/install
- install node 10
- `cd frontend`
- `yarn install`
- `yarn start`
- `cd backend`
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver`

#### Frontend Guideline
- when you need to add a script for a new page add a new `entry` to `webpack.config.json
- for global scripts and styles use the `global` entry

#### Frontend Integration with DevTools
- open devtools and add the `frontend` folder as a workspace
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
- `cd backend`
- `docker-compose up web`

#### .env
- add the `.env` file in the run configuration in the `EnvFile` tab (press Cmd+Shift+. to see hidden files in the Mac OS X file dialog)


### Development Notes
- Don't modify the default_plugins - if you want to use one copy past it into another place. And place it into a different plugin module, eg with the project name.


### what.digital Packages
- https://pypi.org/project/django-env-settings/
- https://pypi.org/project/django-testuser/
