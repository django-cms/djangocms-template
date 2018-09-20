window.Raven = require('raven-js');
window.Raven
    .config('https://00f24717f70d4cd3927a62922c50261b@sentry.io/1269056')
    .install();

// this will let us have a global jQuery object
window.$ = window.jQuery = require("jquery");

// Modernizr global :)
window.Modernizr = require('modernizr');

window.moment = require('moment');

require('bootstrap');

// this loads the django csrf protection methods for sending forms
require('./js/getcookie.js');

// this is for responsive javascript (adds classes to the body element and sends js events on window resize)
// incompatible with IE, therefore deactivated for the time being.
// require('./js/rsp.js');


// template npm libs

window.enquire = require('enquire.js');
window.FastClick = require('fastclick');
require('jquery-debouncedresize');
require('imagesloaded');
require('jquery-match-height');
window.Cookies = require('js-cookie');
window.svg4everybody = require('svg4everybody');
require('object-fit-images');
window.autosize = require('autosize');
require('ekko-lightbox');
require('../node_modules/ekko-lightbox/dist/ekko-lightbox.css');
require('basictable');
require('../node_modules/basictable/basictable.css');

// template
require('./js/lightbox');
require('./js/responsive-tables');

// Styles
require('./scss/index.sass');

// Fonts

require('./fonts/stylesheet.css');

// Icons

require('@fortawesome/fontawesome-free/scss/fontawesome.scss');
require('@fortawesome/fontawesome-free/scss/brands.scss');
require('@fortawesome/fontawesome-free/scss/solid.scss');
require('@fortawesome/fontawesome-free/scss/regular.scss');

// Django CMS Refresh helper
// https://github.com/divio/django-cms/issues/6273
require('./js/djangocms-reload');

