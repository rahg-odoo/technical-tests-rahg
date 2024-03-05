from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    volume = fields.Float(string="Volume", compute="_compute_volume")
    weight = fields.Float(string="Weight", compute="_compute_weight")

    def _compute_volume(self):
        for record in self:
            record.volume = 0
            for product in record.move_ids:
                record.volume += product.product_id.volume * product.quantity

    def _compute_weight(self):
        for record in self:
            record.weight = 0
            for product in record.move_ids:
                record.weight += product.product_id.weight * product.quantity


