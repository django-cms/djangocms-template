declare var CMS: any


if (window.hasOwnProperty('CMS')) {
    CMS.$(window).on('cms-content-refresh', () => {
        $('script[data-cms-reload]').each(() => {
            let src = $(this).attr('src')
            $(this).remove()
            $('<script>').attr('src', src).appendTo('head')
        })
    })
}
