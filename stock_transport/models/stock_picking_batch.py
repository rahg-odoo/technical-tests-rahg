from odoo import models, fields, api


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one(string="Dock", comodel_name='fleet.dock')
    vehicle_id = fields.Many2one(
        string="Vehicle", comodel_name='fleet.vehicle')
    vehicle_category_id = fields.Many2one(
        comodel_name='fleet.vehicle.model.category', string="Vehicle Category")
    weight = fields.Float(string="Weight", compute='_compute_weight')
    volume = fields.Float(string="Volume", compute='_compute_volume')
    lines = fields.Integer(string="Lines", compute="_compute_lines", store="1")
    transfers = fields.Integer(
        string="Transfers", compute="_compute_transfer", store="1")

    @api.onchange('vehicle_id')
    def _onchange_for_vehicle_category(self):
        for record in self:
            record.vehicle_category_id = record.vehicle_id.category_id

    @api.depends('vehicle_id')
    def _compute_weight(self):
        for record in self:
            s = sum(record.move_line_ids.product_id.mapped('weight'))
            if record.vehicle_category_id.max_weight:
                record.weight = (
                    s / record.vehicle_category_id.max_weight) * 100
            else:
                record.weight = 0

    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
            record.lines = len(record.move_line_ids)

    @api.depends('picking_ids')
    def _compute_transfer(self):
        for record in self:
            record.transfers = len(record.picking_ids)

    @api.depends('vehicle_id')
    def _compute_volume(self):
        for record in self:
            s = sum(record.move_line_ids.product_id.mapped('volume'))
            if record.vehicle_category_id.max_volume:
                record.volume = (
                    s / record.vehicle_category_id.max_volume) * 100
            else:
                record.volume = 0
