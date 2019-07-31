
/*
 * Custom Styles Config File for ckeditor
 * Mario Colombo (mario@what.digital)
 */


/*
 * DOCS: http://docs.ckeditor.com/#!/api/CKEDITOR.dtd
 */

CKEDITOR.config.fontSize_sizes = '0.5em;0.6em;0.7em;0.8em;0.9em;1.1em;1em;1.2em;1.3em;1.4em;1.5em;1.6em;2em;2.3em;2.5em;3em;4em;5em;6em;7em';

CKEDITOR.stylesSet.add('default', [
    {
        'name': 'float left', 'element': 'span', 'attributes': {'class': 'float-left'}
    },
    {
        'name': 'Force black color', 'element': 'span', 'attributes': {'class': 'rte-black'}
    },
    {
        'name': 'normal line height', 'element': 'div', 'attributes': {'class': 'line-height-1'}
    },
    {
        'name': 'List style Example', 'element': 'ul', 'attributes': {'class': 'rte-list-style'}
    },
    {
        'name': 'table style example', 'element': 'table', 'attributes': {'class': 'rte-table-style'}
    },
]);

CKEDITOR.dtd.$removeEmpty.span = false;

CKEDITOR.config.allowedContent = true;
