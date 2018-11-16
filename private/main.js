import * as Sentry from '@sentry/browser';

Sentry.init({
  dsn: 'https://cfae66c325fa485cbd821fdf5cf994d4@sentry.io/1269040',
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

