
// this will let us have a global jQuery object
window.$ = window.jQuery = require("jquery");

// Modernizr global :)
window.Modernizr = require('modernizr');

window.moment = require('moment');

require('bootstrap');

// this loads the django csrf protection methods for sending forms
require('./js/getcookie.js');


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


// Bootstrap
require('./scss/libraries/bootstrap4.sass');
require('./scss/libraries/font-awesome.sass');

// Icons
require('@fortawesome/fontawesome-free/scss/fontawesome.scss');
require('@fortawesome/fontawesome-free/scss/brands.scss');
require('@fortawesome/fontawesome-free/scss/solid.scss');
require('@fortawesome/fontawesome-free/scss/regular.scss');
