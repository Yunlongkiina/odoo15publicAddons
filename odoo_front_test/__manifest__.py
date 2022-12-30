# -*- coding: utf-8 -*-
{
    'name': "odooFrontTest",
    'summary': """
        To test how odoo front interact with backend
        """,
    'description': """
        To test how odoo front interact with backend
        """,
    'author': "Yunlong Liu",
    'website': "http://www.example.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "sale", "sale_management"],
    # always loaded
    'assets': {
        'web.assets_qweb': ['/odoo_front_test/static/src/js/components/PartnerOrderSummary.xml'],
        'web.assets_backend': [
            '/odoo_front_test/static/src/js/components/pop.js',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sales_data_template.xml',
        'views/order_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
