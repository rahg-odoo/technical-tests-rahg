# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Bridge For Stock Transport',
    'version': '1.0',
    'sequence': 51,
    'description': "To provide download option",
    'depends': ['stock'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'views/res_config_settings_views.xml'
    ]
}
