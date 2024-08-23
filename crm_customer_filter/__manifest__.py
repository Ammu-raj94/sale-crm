# -*- coding: utf-8 -*-

{
    'name': 'CRM Customer Filter',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': """CRM sales person filter.""",
    'depends': ['base','crm'],
    'data': ['views/crm_lead_views.xml'],
    'assets': {
        'web.assets_backend': {
            '/crm_customer_filter/static/src/xml/customer_filter.xml',
            '/crm_customer_filter/static/src/js/customer_filter.js',
        },
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
