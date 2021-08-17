### Frontend Guidelines

- the project-specific scss styles can be in `global`, it's acceptable, but the js logic with big imports must not be
- when you need to add a script (with additional external dependencies) for a new component add a new `entry` in `webpack.config.js` and a component sub module
- for global scripts and styles use the `global` entry, and add the respective HTML code in your template, see the `frontend/components/demo-plugin` example
- if you need to add a global variable to JS, add it to `backend/templates/base.html#django` const and extend `frontend/global/ts/django.ts#django`
- if you need to add a static file, eg on url `https://localhost/static/global/img/icon.png` - add it to `frontend/global/img`, everything in there will be accessible on url `/static/`
- we must use 24 columns config in bootstrap 4
- make sure that you have a bs4 `container` alternative on any body html, because editors want to use Row/Column plugins in any place of the page, which works only inside a `container` class. Often you also need to remove the padding or create your own `container` alternative, use `@include make-container();` mixin for those cases. Also make sure that Container bs4 cms plugin always behaves as a container class, eg with `@include make-container();`
- keep the comments in `package.json` intact, ie don't use `yarn add` command
- prefer to keep scss in `frontend/global/`, since it's easier when it's all in one place, unless you need to import something that has a noticeable influence on the `global` pack compilation size
- for import of svg or image files in scss use something as `background: url('~global/img/dot-line/short-blue.svg')`;

#### On page reload

Remember that every time an editor changes a plugin on a page, almost the whole body is dropped from DOM and added anew using AJAX. That's why if you have any scripts that are attached to those DOM elements you have to reattach them to `cms-content-refresh` DOM event.

At the same time you cannot just do `document.addEventListener('DOMContentLoaded', () => {}, {once: true})` or `$(document).on('ready', () => {})`. On `cms-content-refresh` you have to make sure that your events are firstly removed from DOM with `removeEventListener`, otherwise your listener are going to accumulate indefinitely, and in the end you'll be attaching eg your navbar 15 times on every page edit, and the browser is going to kill the tab because of overload.

Once you drop your event using `removeEventListener` you must then attach it again with `document.addEventListener('DOMContentLoaded', () => {})`.

Example:
```javascript
function initGalleryPlugin() {
    $('#image-plugin').lightGallery();
}
document.removeEventListener('DOMContentLoaded', initGalleryPlugin);
document.addEventListener('DOMContentLoaded', initGalleryPlugin);
```

#### Fonts

- use https://google-webfonts-helper.herokuapp.com/fonts/ to download the web font from google (set the relative path to empty string in the configurator)
- if you have TTFs but no web font use https://www.fontsquirrel.com/tools/webfont-generator to create one
- add a directory for font files, eg `frontend/global/fonts/frutiger/` with files as `frutiger.css`, `frutiger.woff2`, `frutiger.woff` (if ie11 is needed), etc
- in `frutiger.css` import the other files as following
```css
@font-face {
    font-family: 'Frutiger';
    src: url('frutiger.woff2') format('woff2'),
         url('frutiger.woff') format('woff');
}
```
- import it in a global scss file, eg `frontend/global/scss/text.scss` as `@import '~global/fonts/frutiger/frutiger.css';`

Make sure to not add them into index.js, add them to an scss. Otherwise the fonts are going to be invisible in CKEditor.

#### IE 11 support

If you need IE 11 support in your project then add babel to your `package.json` (use the latest versions if needed): 
```json
"babel-loader": "^8.1.0",
    "@babel/preset-env": "^7.11.0",
    "@babel/preset-typescript": "^7.10.4",
    "@babel/plugin-syntax-dynamic-import": "^7.8.3",
    "@babel/plugin-proposal-decorators": "^7.10.5",
    "@babel/plugin-proposal-class-properties": "^7.10.4",
    "@babel/plugin-transform-spread": "^7.12.1",
    "core-js": "^3.6.5",
    "regenerator-runtime": "^0.13.7"
```
And update the webpack config with babel-loader configuration:
```javascript
    target: ['web', 'es5'],
    module: {
        rules: [
            ...
            {
                test: /\.(tsx?|jsx?|js?)$/,
                loader: 'babel-loader',
                exclude: [
                    /node_modules/,
                ],
                options: {
                    presets: [
                        [
                            '@babel/preset-env',
                            {
                                'modules': false,
                                'targets': {'browsers': ['ie >= 11', 'not dead']},
                            }
                        ],
                        '@babel/preset-typescript',
                    ],
                    plugins: [
                        ['@babel/plugin-proposal-decorators', {'legacy': true}],
                        ['@babel/plugin-proposal-class-properties', {'legacy': true}],
                        ['@babel/plugin-transform-arrow-functions', {'legacy': true}],
                        '@babel/plugin-syntax-dynamic-import',
                        '@babel/plugin-transform-spread'
                    ],
                },
            },
    },
```
