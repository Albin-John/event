from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class EventEvent(models.Model):
    _inherit = "event.event"

    staff_ids = fields.One2many(
        comodel_name="event.staff", inverse_name="event_id", string="Staffs",
    )
    staff_count = fields.Integer(
        compute="_compute_staff_count", string="Total event staffs", store=True,
    )

    @api.depends("staff_ids")
    def _compute_staff_count(self):
        for event in self:
            event.staff_count = len(event.staff_ids)