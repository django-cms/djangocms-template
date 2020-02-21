# Web Fonts

## 1. Download the Web Font

### Google Fonts

- use https://google-webfonts-helper.herokuapp.com/fonts/ to download the web font from google  (set the relative path to empty string in the configurator)


### Other web fonts

- if you have TTFs but no web font use https://www.fontsquirrel.com/tools/webfont-generator to create one, if you have a web font just proceed to step 2


## 2. install the font
- put the font into frontend/global/fonts/font-name
- put the web font css into font-name.css in frontend/global/fonts/font-name
- add the css to index.js like in this example: `require('./fonts/muli/muli.css');`
