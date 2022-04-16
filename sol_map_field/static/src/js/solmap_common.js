odoo.define('sol_map_field.solmap_common', function () {
    "use strict";
    var SolMapMixin = {
        cssLibs: [
            '/sol_map_field/static/lib/ol-6.4.3/ol.css',
            '/sol_map_field/static/lib/ol-ext/ol-ext.min.css',
        ],
        jsLibs: [
            '/sol_map_field/static/lib/ol-6.4.3/ol.js',
            '/sol_map_field/static/lib/ol-ext/ol-ext.min.js',
        ],
    };

    return {
        SolMapMixin: SolMapMixin,
    };
});