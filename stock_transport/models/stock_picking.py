from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    volume = fields.Float(string="Volume", compute="_compute_volume")
    weight = fields.Float(string="Weight", compute="_compute_weight")

    def _compute_volume(self):
        for record in self:
            record.volume = sum(record.move_ids.mapped('product_id.volume'))

    def _compute_weight(self):
        for record in self:
            record.weight = sum(record.move_ids.mapped('product_id.weight'))
