# Copyright 2021-Today Albin John<albinjohn54@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class EventStaff(models.Model):
    _name = "event.staff"
    _description = "Event Staff"

    contact = fields.Many2one("res.partner", string="Contact", required=True)
    role = fields.Many2one("event.staff.role", string="Role")
    event_id = fields.Many2one("event.event", string="Event", required=True)
    note = fields.Text()

    @api.model
    def create(self, vals):
        event_staff_id = super(EventStaff, self).create(vals)
        if event_staff_id:
            attendee = self.env["event.registration"].create(
                {
                    "partner_id": event_staff_id.id,
                    "event_id": event_staff_id.event_id.id,
                }
            )
            attendee._onchange_partner()
            attendee.confirm_registration()
        return event_staff_id
