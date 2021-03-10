import * as Sentry from '@sentry/browser';


Sentry.init({
    dsn: '',
    environment: DJANGO_ENV,
});


window.$ = window.jQuery = require('jquery');

require('bootstrap');
require('./main.scss');

// djangocms-bootstrap4 icons
require('@fortawesome/fontawesome-free/scss/fontawesome.scss');
require('@fortawesome/fontawesome-free/scss/brands.scss');
require('@fortawesome/fontawesome-free/scss/solid.scss');
require('@fortawesome/fontawesome-free/scss/regular.scss');
