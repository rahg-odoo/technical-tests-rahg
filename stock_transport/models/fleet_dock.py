from odoo import models, fields, api


class FleetDock(models.Model):
    _name = "fleet.dock"
    _description = "add dock"
    
    name = fields.Char(string="Dock")