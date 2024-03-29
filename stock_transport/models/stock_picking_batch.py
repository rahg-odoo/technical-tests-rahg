from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one(string="Dock", comodel_name='fleet.dock')
    vehicle_id = fields.Many2one(
        string="Vehicle", comodel_name='fleet.vehicle')
    vehicle_category_id = fields.Many2one(
        comodel_name='fleet.vehicle.model.category', string="Vehicle Category")
    weight = fields.Float(
        string="Weight", compute='_compute_weight', store=True)
    volume = fields.Float(
        string="Volume", compute='_compute_volume', store=True)
    lines = fields.Integer(string="Lines", compute="_compute_lines", store="1")
    transfers = fields.Integer(
        string="Transfers", compute="_compute_transfer", store="1")

    w = fields.Float(
        string="Weight", compute='_compute_w')
    v = fields.Float(
        string="Volume", compute='_compute_v')

    # _sql_constraints = [
    #     ('check_volume', 'CHECK( v >= )', 'checking volume'),
    #     ('check_weight', 'CHECK( w >= )', 'checking weight')
    # ]

    @api.constrains('v','vehicle_category_id')
    def check_volume(self):
        for record in self:
            if record.v > record.vehicle_category_id.max_volume:
                raise ValidationError('volume must be less than max volume capacity of vehicle')
    
    @api.depends('weight', 'volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.weight} Kg,{record.volume} m3, {record.vehicle_id.driver_id.name})"

    @api.onchange('vehicle_id')
    def _onchange_for_vehicle_category(self):
        for record in self:
            record.vehicle_category_id = record.vehicle_id.category_id

    @api.depends('vehicle_id')
    def _compute_weight(self):
        for record in self:
            s = sum(record.move_line_ids.product_id.mapped('weight'))
            if record.vehicle_category_id.max_weight:
                record.weight = round((
                    s / record.vehicle_category_id.max_weight) * 100, 2)
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
                record.volume = round((
                    s / record.vehicle_category_id.max_weight) * 100, 2)
            else:
                record.volume = 0

    @api.depends('vehicle_id')
    def _compute_w(self):
        for record in self:
            s = 0
            for line in record.move_line_ids:
                s += line.quantity * line.product_id.weight
            record.w = s

    @api.depends('vehicle_id')
    def _compute_v(self):
        for record in self:
            s = 0
            for line in record.move_line_ids:
                s += line.quantity * line.product_id.volume
            record.v = s
