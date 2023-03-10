# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Yunlong Liu",
    'category': 'Hospital',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/patient_appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/operation_view.xml',
        'views/menu.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_learning_hospital_management/static/src/css/patient_form_view.css',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False
}
