import * as Sentry from '@sentry/browser';

// TODO: update Sentry DSN here
Sentry.init({
  dsn: 'https://12324@sentry.io/12324',
});



// template
require('./js/lightbox');
require('./js/responsive-tables');

// Styles
require('./scss/index.sass');

// Fonts

require('./fonts/stylesheet.css');


// Django CMS Refresh helper
// https://github.com/divio/django-cms/issues/6273
require('./js/djangocms-reload');

