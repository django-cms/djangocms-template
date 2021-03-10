import {initReloadScriptsOnContentRefresh} from 'global/ts/reload-scripts-on-content-refresh';
import * as Sentry from '@sentry/browser';


try {
    document.removeEventListener('DOMContentLoaded', initScripts);
} catch (error) {
    // todo try catch might be redundant
}
document.addEventListener('DOMContentLoaded', initScripts);


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
