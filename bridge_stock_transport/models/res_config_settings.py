# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models, api, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean("Dispatch Management System")
