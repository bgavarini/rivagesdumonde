# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import api, fields, models
from odoo.tools.translate import _


class Pontoon(models.Model):
    """Manage 'pontoon' model."""
    _name = "pontoon"

    ################
    # DISPLAY NAME #
    ################

    # name = fields.Char(string="Name", compute="compute_name")
    name = fields.Char(string="Name")

    @api.multi
    def compute_name(self):
        """Compute the 'name' field value of some 'pontoon'."""
        for record in self:
            record.name = _("Pontoon n°%s") % record.id

    ########
    # BOAT #
    ########

    boat_id = fields.Many2one(comodel_name="boat", string="Boat", required=True)

    ##########
    # CABINS #
    ##########

    cabin_ids = fields.One2many(comodel_name="cabin", inverse_name="pontoon_id", string="Cabins")
