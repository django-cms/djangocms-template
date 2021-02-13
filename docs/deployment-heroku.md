Project Setup
-------------------------------------------------------------------------------

- `heroku login`
- `heroku apps:create {project_name}-staging`
- `heroku addons:create heroku-postgresql:hobby-dev`
- `heroku config:set DJANGO_SETTINGS_MODULE=backend.settings`
- `heroku config:set DEFAULT_STORAGE_DSN=s3://AKIAJEUDGSDEAOPFL54RDQ:75n4grTvRpu0YsdgwFv2HxJZ/lGUhN@djangocms-template-staging.s3.eu-central-1.amazonaws.com/?auth=s3v4&domain=djangocms-template-staging.s3.eu-central-1.amazonaws.com --remote staging --app={project_name}-staging`
- `heroku config:set STAGE=test --remote staging --app={project_name}-staging`
- `heroku config:set DEBUG=true --remote staging --app={project_name}-staging`
- `git push heroku master`
  
Production
- `heroku apps:create {project_name}-production`
