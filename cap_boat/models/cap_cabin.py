# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import api, fields, models
from odoo.tools.translate import _


class Cabin(models.Model):
    """Manage 'cabin' model."""
    _name = "cabin"

    ################
    # DISPLAY NAME #
    ################

    # name = fields.Char(string="Name", compute="compute_name")
    name = fields.Char(string="Name")

    @api.multi
    def compute_name(self):
        """Compute the 'name' field value of some 'cabin'."""
        for record in self:
            record.name = _("Cabin n°%s") % record.id

    ########
    # BOAT #
    ########

    boat_id = fields.Many2one(comodel_name="boat", string="Boat", required=True)

    @api.model
    @api.onchange("boat_id")
    def onchange_boat_id(self):
        """Manage on the fly a new 'boat_id' field value of one 'cabin'."""
        if self.pontoon_id.id not in self.boat_id.pontoon_ids.ids:
            self.pontoon_id = self.env["pontoon"]
        return {"domain": {"pontoon_id": self.domain_pontoon_id()}}

    ###########
    # PONTOON #
    ###########

    pontoon_id = fields.Many2one(comodel_name="pontoon", string="Pontoon", required=True)

    @api.model
    def domain_pontoon_id(self):
        """Return the 'pontoon_id' field domain filter of one 'cabin'."""
        return [("id", "in", self.boat_id.pontoon_ids.ids)]

    pontoon_id_invisible = fields.Boolean(compute="compute_pontoon_id_invisible")

    @api.multi
    @api.depends("boat_id")
    def compute_pontoon_id_invisible(self):
        """Compute the 'pontoon_id_invisible' field value of some 'cabin'."""
        for record in self:
            record.pontoon_id_invisible = not record.boat_id

    ##########
    # MATRIX #
    ##########

    x = fields.Integer(string="x")
    y = fields.Integer(string="y")

    #########
    # PRICE #
    #########

    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")

    amount = fields.Monetary(string="Amount", currency_field="currency_id")

    color = fields.Char(string="Color")

    ############
    # RESERVED #
    ############

    is_reserved = fields.Boolean(string="Reserved")
