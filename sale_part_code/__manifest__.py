# -*- coding: utf-8 -*-

{
    'name': "Sale Part Code",
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': """Sale part code for Products""",
    'description': "Allows to add sale part code in Products and search product"
                   "based on that field in sale order line.",
    'depends': ['sale_management'],
    'data': [
        'views/product_product_views.xml',
        'views/product_template_views.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install ': False,
    'application': False
}
