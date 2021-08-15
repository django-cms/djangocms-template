2021.08
-------------------------------------------------------------------------------
- completely removed the aldryn stack (aldryn-addons, aldryn-django, aldryn-djangocms)
- django CMS 3.9
- abandon custom docker images
- new docker-based build process
- proper whitenoise static files integration
- proper frontend webpack-dev-server hot reload setup
- fix HMR (webpack dev server hot reloading)


2021.06
-------------------------------------------------------------------------------

- Added security settings for CSRF, CSP, HSTS, session cookies
- Recompiled requirements.txt (a few packages updated)
- Updated frontend packages (webpack, webpack-dev-server, bootstrap to 4.6.0, some dependencies)

2021.06
-------------------------------------------------------------------------------

- added default DRF settings: disabled browsable API, default IsAuthenticated permission
- updated django and aldryn-django to version 3.1.12.0
- disabled djangocms-algolia by default (uncomment djangocms_algolia in INSTALLED_APPS to enable)
- updated postgres image to 10.16

2021.03
-------------------------------------------------------------------------------

- added SEO language hrefs
- fixed the django-cms treebeard bug
- fixed frontend sentry loading, now it captures the first scripts execution exceptions
- fixed the issue with frontend components being incorrectly reloaded after a content change, which caused browser memory overload
- fixed CKEditor WYSIWYG styles

2021.02
-------------------------------------------------------------------------------

- recompiled requirements.txt
- bumped aldryn-django to 3.1.7.0
- fixed djangocms-link-all double anchor `#` bug
- fixed frontend building by installing linux package `autoconf`
- upgraded backend & frontend dependencies to incorporate the latest security patches
- optimized dockerfile cache and compilemessages timing
- improved the docker versioning schema
- converted images to webp during webpack build
- added code formatters: prettier for JS and intellij .editorconfig for HTML & SCSS

2021.01
-------------------------------------------------------------------------------

- added a patch for djangocms-link-all that gracefully protects linked pages from deletion
- fixed the disabled HTTPS (it was using .env file to override the server envs)
- fixed webpack CORS issues for fonts and assets
- fixed cache by disabling it for local dev
- disabled django 3.1 sidebar completely

### How to upgrade

##### djangocms-bootstrap4
- update/remove `settings.DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_FIELDSETS` if you used it
- rename `settings.DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_SPACING` to `settings.DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_VERTICAL_SPACING_EXTERNAL`, consider adding `settings.DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_VERTICAL_SPACING_EXTERNAL`
- review the bootstrap4 container plugin interface to confirm that the new fields look as you expect them to
- if you used bootstrap4 container plugin `width_external` field - add migrations that drop it, it is no longer useful

##### djangocms-link-all
- add `settings.LINK_ALL_PLUGINS` variable in accordance with `link_all.settings.LINK_ALL_PLUGINS` format, otherwise you won't have `cms.Page` protection

2020.12
-------------------------------------------------------------------------------

- dropped aldryn-django static serving, uwsgi, middleware
- added heroku support & guidelines
- improved the deployment speed - from 12m to 6.5m
- added .flake8 and isort configurations
- upgraded webpack-dev-server to 4.0.0-beta, which adds webpack 5 support


2020.11
-------------------------------------------------------------------------------

- upgraded to python 3.9, django-cms 3.8, django 3.1.3, nodejs 14, webpack 5, typescript 4
- upgraded to djangocms-blog 1.2
- dropped aldryn-translation-tools
- dropped divio wheels support

2020.10
-------------------------------------------------------------------------------

- fixed the content caching which was set to 5m by default - set it to 4h, and set menus and permissions cache to 1h
- fixed the default django caching which was disabled completely - set it to 4h
- switched to django-environ instead of the custom env packages
- added `manage.py clear_cache` to `settings.MIGRATION_COMMANDS`

#### Breaking Changes
- upgraded to python 3.7 by basing the docker image on divio/base:0.7-py3.7-slim-stretch
- upgraded to DjangoCMS 3.8 and Django 3.1
- changed the stage anonymous access url from `https://{base}/?guest-view=true` to `https://{base}/?anonymous-access=true`
- changed `settings.ALGOLIA_SEARCH_INDEX_TEXT_LIMIT` to `95_000`


2020.09
-------------------------------------------------------------------------------

#### Breaking Changes
- renamed DivioEnv to DjangoEnv, as well as the related variables in settings.py
- dropped bootstrap4 link plugin in favor of djangocms-link-all
- move addons/ and addons-dev/ directories into backend/


2020.08
-------------------------------------------------------------------------------

- added a new image plugin with better UX
- updated the link plugin - mainly UX improvement

#### Breaking Changes

- changed the directory structure in order to stay closer to the django standards
    - although a complete normalization to django ecosystem is still impossible due to the hardcoded deviations within divio bot and aldryn-django codebase (eg for addons, addons-dev, wsgi.py, etc)
- renamed the js `window.DJANGO` variable to `window.django` which already exists in django


2020.07
-------------------------------------------------------------------------------

- added a new link plugin that allows to select the link type - eg blog article, cms page, external url, etc
- added ability to use html links and iframe to the CMS text editor
- added better styles compatibility with outdated browsers as safari, ie11, etc
- cms dynamic forms:
    - fixed the email variables representation and validation
    - fixed django success message that was shown on an unrelated page, seemingly on random
    - fixed the form submission success message that could have been invisible for the user, now the page scrolls to it after the form submission request
- fixed spellchecker in the CMS text editor

### Technical

- added a wrapper for [linkit](https://github.com/dreipol/linkit) with djangocms-blog support, located at `backend.plugins.link`
- added backend.site_config example
- added django-sortedm2m for simple sorting M2M models - it's possible with django-admin-sortable2 but the complexity is unreasonable
- added test of pages on the real database that fully rollbacks a divio deployment if any page returns a 5XX code 
- updated docker base image to from 4.16 to 4.17
- fixed django translations
- fixed `<html>`'s tag `lang` attribute, it was empty before
- fixed aldryn-sso email duplication issue on divio database export
- fixed webpack autoprefixer config, before it wasn't working
- disabled the ability of search engines to index the aldryn-sso login page
- dropped sentry config in settings and use the version from aldryn-django
- dropped custom ckeditor toolbar to avoid issues as missing spellchecker
- upgraded package.json packages

#### Breaking Changes

- updated aldryn-forms from 5th to 6th version that contains a lot of fixes, eg we disabled the original Form plugin

### Documentation

- updated backend.md
- updated frontend.md

2020.06
-------------------------------------------------------------------------------

- added [djangocms-socialshare](https://gitlab.com/what-digital/djangocms-socialshare) - a plugin for customizable rendering of sharing and social links icons
- added [djangocms-algolia](https://gitlab.com/victor.yunenko/djangocms-algolia)
- added [linkit](https://github.com/dreipol/linkit) that must be used for all links from now on
- fixed the `login with divio` feature that used to raise an "email duplicate error" ([divio/aldryn-sso#66](https://github.com/divio/aldryn-sso/issues/66))
- fixed the freezing of page after 5-10 CMS edits
- fixed django-cms (or aldryn-django) local caching issue

### Breaking Changes

- replaced `backend.articles` with djangocms-blog
- moved out `backend.tests.test_pages` into djangocms-helpers 2.2
- moved `backend.plugins.default` to `backend.plugins` for simplification
- deleted `bs4_card_columns`, because it appears that it requires styles and we've haven't seen a request from the client to style it
