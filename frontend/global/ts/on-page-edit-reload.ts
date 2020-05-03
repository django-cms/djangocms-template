declare var CMS: any;


export function main() {
    const isCmsPresent = window.hasOwnProperty('CMS');
    if (isCmsPresent) {
        initScriptReloadListener();
    }
}


function initScriptReloadListener() {
    const cmsPageEditedEvent = 'cms-content-refresh';
    CMS.$(window).on(cmsPageEditedEvent, () => {
        $('script[data-is-reload-on-page-edit]').each((index, element) => {
            forceScriptReload.call(element);
        })
        window.document.dispatchEvent(new Event('DOMContentLoaded', {
            bubbles: true,
            cancelable: true,
        }));
    })
}


function forceScriptReload() {
    const scriptSrc = $(this).attr('src') as string;
    $(this).remove();
    $('<script>').attr('src', scriptSrc).appendTo('head');
}
