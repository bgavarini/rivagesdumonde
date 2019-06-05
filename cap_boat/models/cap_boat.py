# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import api, fields, models
from odoo.tools.translate import _


class Boat(models.Model):
    """Manage 'boat' model."""
    _name = "boat"

    ################
    # DISPLAY NAME #
    ################

    # name = fields.Char(string="Name", compute="compute_name")
    name = fields.Char(string="Name")

    @api.multi
    def compute_name(self):
        """Compute the 'name' field value of some 'boat'."""
        for record in self:
            record.name = _("Boat n°%s") % record.id

    #########
    # IMAGE #
    #########

    image = fields.Binary(string="Image")

    ############
    # PONTOONS #
    ############

    pontoon_ids = fields.One2many(comodel_name="pontoon", inverse_name="boat_id", string="Pontoons")
