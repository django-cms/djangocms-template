/**
 * Created by mario on 7/20/16.
 */


// standard django csrf protection
// https://docs.djangoproject.com/en/1.9/ref/csrf/


// setting this globally might collide with some DjangoCMS admin forms (TextField text-mode plugins)
// This is unconfirmed
// TODO: confirm this issue

// var csrftoken = getCookie('csrftoken');


// jQuery.ajaxSetup({
//       beforeSend: function (xhr, settings) {
//           if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//               xhr.setRequestHeader("X-CSRFToken", csrftoken);
//           }
//       }
// });

// using jQuery
window.getCookie = function(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

window.csrfSafeMethod = function(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

window.csrftoken = getCookie('csrftoken');
