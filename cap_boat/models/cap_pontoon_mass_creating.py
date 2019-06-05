# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import api, fields, models

from odoo.exceptions import UserError
from odoo.tools.translate import _


class PontoonMassCreating(models.TransientModel):
    """Manage 'pontoon.mass_creating' model."""
    _name = "pontoon.mass_creating"

    ############
    # QUANTITY #
    ############

    pontoon_qty = fields.Integer(string="Pontoon Quantity To Create")

    @api.onchange("pontoon_qty")
    def onchange_pontoon_qty(self):
        """Manage on the fly a new 'pontoon_qty' field value of one 'pontoon.mass_creating'."""
        # MANAGE NEGATIVE QUANTITY
        if self.pontoon_qty < 0:
            self.pontoon_qty = 0

    ##########################################
    # ACTIONS AND OTHER NON CORE ORM METHODS #
    ##########################################

    def mass_creating(self):
        """Create in mass some 'pontoon'."""
        # LIMIT WIZARD TO ONLY ONE ACTIVE ID
        if len(self.env.context["active_ids"]) > 1:
            message = _("You should not use these wizard for several boats at once.")
            raise UserError(message)
        # CREATE PONTOONS
        for active_id in self.env.context["active_ids"]:
            args = {"boat_id": active_id}
            for i in range(self.pontoon_qty or 0):
                self.env["pontoon"].create(args)
