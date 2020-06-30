import {initOnPageEditReloadScript} from 'global/ts/on-page-edit-reload';


document.addEventListener(
    'DOMContentLoaded',
    () => {
        initOnPageEditReloadScript();
    },
    {once: true},
)
