The default testing user for non-prod environment: test@what.digital / test@what.digital


## Setup
- install yarn https://yarnpkg.com/en/docs/install
- `yarn install`
- `yarn start`
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver`


## Docker
- There is docker support so that you dont have to set up a python virtual 
environment on your host
- Install docker on your machine (including docker-compose)
- Run `docker-compose up web`


## Pycharm
- add the `.env` file in the run configuration in the `EnvFile` tab (press Cmd+Shift+. to see hidden files in the Mac OS X file dialog)
