import {initReloadScriptsOnContentRefresh} from 'global/ts/reload-scripts-on-content-refresh';
import * as Sentry from '@sentry/browser';


document.removeEventListener('DOMContentLoaded', initScripts);
document.addEventListener('DOMContentLoaded', initScripts, {once: true});


function initScripts() {
    tryScriptExecution(initReloadScriptsOnContentRefresh);
}


function tryScriptExecution(callable: CallableFunction) {
    try {
        callable()
    } catch (error) {
        Sentry.captureException(error);
    }
}
