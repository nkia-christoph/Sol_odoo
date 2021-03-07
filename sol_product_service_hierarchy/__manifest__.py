{
    'name': "Service Hierarchy",
    "category": "sale",
    'author': "0Solver0",
    'license': 'AGPL-3',
    'version': '13.0',
    'summary':"""This module allow user to create a hierarchy of service""",
    'description':""" 
        Features
            * Compose a service from several sub services.
            * Sub service can be inserted automatically in sale order line : (Field include price)
            * Sub service can be shared with all services : (Field Product shared).
            * Sub service can add extra price to the composed service in sale order line : (Field include price).
            * Sub service can add extra space to service description in sale order line : (Field extra space).
            """,
    'depends': [
        'base',
        'sale_management'
    ],
    'data': [
        'wizard/import_products_form.xml',
        'view/product_template.xml',
        'view/so_line_service_hierarchy_fv.xml',
        'view/so_line_service_hierarchy_print.xml',
    ],
    'test' :  [ ],
    'css'  :  [ ],
    'demo' :  [ ],
    'installable' : True,
    'application' :  False,
    "images":['static/description/icon.png'],
}
