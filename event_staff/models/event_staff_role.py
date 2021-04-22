# Copyright 2021-Today Albin John<albinjohn54@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class EventStaffRole(models.Model):
    _name = "event.staff.role"
    _description = "Event Staff Role"

    name = fields.Char(string="Name", required=True)
