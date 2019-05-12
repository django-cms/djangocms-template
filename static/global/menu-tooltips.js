jQuery(document).ready(function () {

    jQuery('.with-submenu').each(function () {
        jQuery(document).on('click', function (ev) {
            if (!jQuery(ev.target).parents('.popover').length && !jQuery(ev.target).parents('.with-submenu').length) {
                jQuery('.with-submenu').popover('hide');
            }
        });

        jQuery(this).click(function (event) {
            event.preventDefault();
        });

        jQuery(this).popover({
            content: jQuery(this).find(".submenu"),
            html: true,
            placement: "bottom",
            trigger: 'click',
        })
    });
});

