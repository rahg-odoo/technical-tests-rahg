# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Transport',
    'version': '1.0',
    'sequence': 50,
    'description': "Monday TEST",
    'depends': ['fleet', 'stock_picking_batch'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_views.xml',
        'views/fleet_dock_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml'
    ]
}
