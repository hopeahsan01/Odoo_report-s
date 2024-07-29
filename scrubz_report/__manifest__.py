# -*- coding: utf-8 -*-
{
    'name': "Scrubz Report",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
    Scrubz Quotation Report 
    """,

    'author': "HAK Technologies",
    'website': "https://www.haktechnologies.com",
    'version': '0.1',
    'license': 'OPL-1',
    'images': ['description/icon.png'],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
