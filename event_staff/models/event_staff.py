# Copyright 2021-Today Albin John<albinjohn54@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class EventStaff(models.Model):
    _name = "event.staff"
    _description = "Event Staff"

    contact = fields.Many2one("res.partner", string="Contact", required=True)
    role = fields.Many2one("event.staff.role", string="Role")
    event_id = fields.Many2one("event.event", string="Event", required=True)
