declare var CMS: any;


/**
 * It's a cms reloading fix, probably was written by Mario. What it fixes and whether it's actual right now is unclear.
 */
if (window.hasOwnProperty('CMS')) {
    CMS.$(window).on('cms-content-refresh', () => {
        $('script[data-cms-reload]').each(() => {
            let src = $(this).attr('src');
            $(this).remove();
            $('<script>').attr('src', src).appendTo('head');
        })
    })
}
