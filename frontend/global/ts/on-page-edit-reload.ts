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
    })
}


function forceScriptReload() {
    const scriptSrc: string = $(this).attr('src');
    $(this).remove();
    $('<script>').attr('src', scriptSrc).appendTo('head');
}
