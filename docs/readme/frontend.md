### Frontend Guidelines
- when you need to add a script for a new page/block add a new `entry` in `webpack.config.js` and a page/block sub module
- for global scripts and styles use the `global` entry, and add the respective HTML code in your template
- if you need to add a global variable to JS, add it to `backend/templates/default.html#DJANGO` const and extend `frontend/global/ts/django.ts#DJANGO`
- if you need to add a static file, eg on url `https://localhost/static/img/icon.png` - add it to `frontend/`, everything in there will be accessible on url `/static/`
- if something doesn't work ask Victor, he wrote webpack.config.js

### Frontend Integration with DevTools
- open devtools and add the `frontend` folder as a workspace <details><summary>image</summary> ![](/docs/readme/img/front-int-example.png)</details>
- now you can edit the source maps and save the scss using as Ctrl+S or CMD+S - webpack is going to auto reload right away
- you can also set breaking points for debugging directly on ts files
- also the styles view is linked to the source maps <details><summary>image</summary>![](/docs/readme/img/front-linked-styles.png)</details>
