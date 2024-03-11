from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    volume = fields.Float(string="Volume", compute="_compute_volume")
    weight = fields.Float(string="Weight", compute="_compute_weight")

    def _compute_volume(self):
        for record in self:
            s =0
            for product in record.move_ids:
                s += product.product_id.volume *  product.quantity
            record.volume =s
         

    def _compute_weight(self):
        for record in self:
            s =0
            for product in record.move_ids:
                s += product.product_id.weight *  product.quantity
            record.weight =s
