# -*- coding: utf-8 -*-

{
    'name': 'Sol Field Map',
    'version': '15.0',
    'summary': """Widget """,
    'description': 'Widget base module for showing entities in open street map, draw and geocoding',
    'category': 'Extra Tools',
    'author': '0Solver0',
    'company': '0Solver0',
    'website': "0Solver0",
    'depends': ['web'],
    'data': [],
    'qweb': [],
    'images': [],
    'assets': {
        'web.assets_backend': [
            'sol_map_field/static/src/js/solmap_common.js',
            'sol_map_field/static/src/js/map_form.js',
            'sol_map_field/static/src/scss/map_form.scss',
            ],
        'web.assets_qweb': [
            'sol_map_field/static/src/xml/solmapform.xml',
            ],
        },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
