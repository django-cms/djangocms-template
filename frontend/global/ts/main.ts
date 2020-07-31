import {initReloadScriptsOnContentRefresh} from 'global/ts/reload-scripts-on-content-refresh';


// remember to removeEventListener on `DOMContentLoaded`, see more in docs/

document.addEventListener(
    'DOMContentLoaded',
    () => {
        initReloadScriptsOnContentRefresh();
    },
    {once: true},
);

