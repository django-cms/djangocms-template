Admin Panel
-------------------------------------------------------------------------------
The login/password from the the stage and local setups (created by default):
- test@what.digital
- test@what.digital

Development Setup
-------------------------------------------------------------------------------
- built on Python 3.7, Django 2.1, DjangoCMS 3.7
- install yarn https://yarnpkg.com/en/docs/install
- install node 10
- `yarn install`
- `yarn start`
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver`

#### Frontend Guidelines
- when you need to add a script for a new page add a new `entry` to `webpack.config.json
- for global scripts and styles use the `global` entry
- if something doesn't work ask Victor, he wrote webpack.config.js

#### Frontend Integration with DevTools
- open devtools and add the `frontend` folder as a workspace
    <details>
    <summary>image</summary>
    
    ![](/docs/readme/front-int-example.png)
    
    </details>
- now you can edit the source maps and save the scss using as Ctrl+S or CMD+S - webpack is going to auto reload right away
- you can also set breaking points for debugging directly on ts files
- also the styles view is linked to the source maps
    <details>
    <summary>image</summary>
    
    ![](/docs/readme/front-linked-styles.png)
    
    </details>

#### Docker Setup
- might be not working
- `docker-compose build`
- `docker-compose up web`


Development Notes
-------------------------------------------------------------------------------
Don't modify `backend.plugins.default` unless you do that in djangocms-template project - if you want to customize one of them copy-past it into another module, eg `backend.plugins.plugin_name`.

##### Requirements Management
Don't add random packages into requirements.in and package.json. On older projects we have requirements conflicts that can take weeks to resolve, simply because the original developers were throwing trash into the requirements one by one until the issue was gone. Or copy pasted 30 redundant requirements from the old project, and even added them to `INSTALLED_APPS`. 
- If you add a package who's name isn't verbose enough, eg `tqdm` - add a comment about where it's used, to let others know when it can be dropped.
- If you add a package that might be useless but you don't have the time to check - add a comment about it.
