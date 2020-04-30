### Frontend Guidelines
- the project-specific scss styles can be in `global`, it's acceptable, but the js logic must not be
- when you need to add a script for a new page/block add a new `entry` in `webpack.config.js` and a page/block sub module
- for global scripts and styles use the `global` entry, and add the respective HTML code in your template
- if you need to add a global variable to JS, add it to `backend/templates/default.html#DJANGO` const and extend `frontend/global/ts/django.ts#DJANGO`
- if you need to add a static file, eg on url `https://localhost/static/img/icon.png` - add it to `frontend/`, everything in there will be accessible on url `/static/`
- if something doesn't work ask Victor, he wrote webpack.config.js
- if you need to add images or other assets - add under the respective module, eg `global`, `vendor`, `pages/homepage`, etc
- we need to use 24 columns config in bootstrap 4

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
