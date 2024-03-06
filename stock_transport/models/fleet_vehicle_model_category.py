from odoo import fields, api, models


class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string='Max Weight(kg)', default=1)
    max_volume = fields.Float(string='Max Volume(m3)', default=1)

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight} Kg,{record.max_volume} m3)"
