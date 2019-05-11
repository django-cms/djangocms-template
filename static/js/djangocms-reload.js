if (window.hasOwnProperty('CMS')) {
    CMS.$(window).on('cms-content-refresh', function () {
        jQuery('script[data-cms-reload]').each(function () {
            var src = jQuery(this).attr("src");
            jQuery(this).remove();
            jQuery('<script>').attr('src', src).appendTo('head');
        });
    });
}
