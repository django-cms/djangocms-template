declare var CMS: any;


const isCmsPresent = window.hasOwnProperty('CMS');
if (isCmsPresent) {
    initScriptReloadListener();
}


function initScriptReloadListener() {
    const cmsPageEditedEvent = 'cms-content-refresh';
    CMS.$(window).on(cmsPageEditedEvent, () => {
        $('script[data-is-reload-on-page-edit]').each(() => {
            forceScriptReload.call(this)
        })
    })
}


function forceScriptReload() {
    const scriptSrc: string = $(this).attr('src');
    $(this).remove();
    $('<script>').attr('src', scriptSrc).appendTo('head');
}
