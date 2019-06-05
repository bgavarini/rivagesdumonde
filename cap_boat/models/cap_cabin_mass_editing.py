# coding: utf-8]]>
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import api, fields, models


class CabinMassEditing(models.TransientModel):
    """Manage 'cabin._mass_editing' model."""
    _name = "cabin.mass_editing"

    ############
    # CURRENCY #
    ############

    change_currency_id = fields.Boolean(string="Update Currency")

    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")

    currency_id_invisible = fields.Boolean(compute="compute_currency_id_invisible")

    @api.multi
    @api.depends("change_currency_id")
    def compute_currency_id_invisible(self):
        """Compute the 'currency_id_invisible' field value of some 'cabin.mass_editing'."""
        for record in self:
            record.currency_id_invisible = not record.change_currency_id

    ##########
    # AMOUNT #
    ##########

    change_amount = fields.Boolean(string="Update Amount")

    amount = fields.Monetary(string="Amount", currency_field="currency_id")

    amount_invisible = fields.Boolean(compute="compute_amount_invisible")

    @api.multi
    @api.depends("change_amount")
    def compute_amount_invisible(self):
        """Compute the 'amount_invisible' field value of some 'cabin.mass_editing'."""
        for record in self:
            record.amount_invisible = not record.change_amount

    #########
    # COLOR #
    #########

    change_color = fields.Boolean(string="Update Color")

    color = fields.Char(string="Color")

    color_invisible = fields.Boolean(compute="compute_color_invisible")

    @api.multi
    @api.depends("change_color")
    def compute_color_invisible(self):
        """Compute the 'color_invisible' field value of some 'cabin.mass_editing'."""
        for record in self:
            record.color_invisible = not record.change_color

    ############
    # RESERVED #
    ############

    change_is_reserved = fields.Boolean(string="Update Reserved")

    is_reserved = fields.Boolean(string="Reserved")

    is_reserved_invisible = fields.Boolean(compute="compute_is_reserved_invisible")

    @api.multi
    @api.depends("change_is_reserved")
    def compute_is_reserved_invisible(self):
        """Compute the 'is_reserved_invisible' field value of some 'cabin.mass_editing'."""
        for record in self:
            record.is_reserved_invisible = not record.change_is_reserved

    ##########################################
    # ACTIONS AND OTHER NON CORE ORM METHODS #
    ##########################################

    def mass_editing(self):
        """Edit in mass some 'cabin' passed to context."""
        args = {}
        if self.change_currency_id:
            args.update({"currency_id": self.currency_id.id})
        if self.change_amount:
            args.update({"amount": self.amount})
        if self.change_color:
            args.update({"color": self.color})
        if self.change_is_reserved:
            args.update({"is_reserved": self.is_reserved})
        self.env["cabin"].browse(self.env.context["active_ids"]).write(args)
