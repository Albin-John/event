# Copyright 2021-Today Albin John<albinjohn54@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class EventEvent(models.Model):
    _inherit = "event.event"

    staff_ids = fields.One2many(
        comodel_name="event.staff", inverse_name="event_id", string="Staffs",
    )
    staff_count = fields.Integer(
        compute="_compute_staff_count", string="Total event staffs", store=True,
    )
    note = fields.Text()

    @api.depends("staff_ids")
    def _compute_staff_count(self):
        for event in self:
            event.staff_count = len(event.staff_ids)
