# -*- coding: utf-8 -*-
{
    'name': "base module for Geo, Locate and Draw into map for odoo addons",

    'summary': "base module for showing entities in open street map, draw and geocoding",
    'description': """
        base module for showing entities in open street map, draw and geocoding,
    """,
    "category": "Web",
    'author': "0Solver0",
    'version': '0.1',
    'depends': ['web','base_geolocalize'],
    'data': [
         "views/assets.xml",
         "views/data.xml",
         "data/data_data.xml"
    ],
    'images': ['sol_ol_map_draw/static/description/thumbnails.png'],
    'qweb': ['static/src/xml/solmaptemplate.xml','static/src/xml/solmapform.xml'],
    'installable': True,
    'uninstall_hook': 'uninstall_hook',
    'auto_install': False
}
