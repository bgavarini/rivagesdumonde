# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import api, fields, models


class CabinMassReserving(models.TransientModel):
    """Manage 'cabin.mass_reserving' model."""
    _name = "cabin.mass_reserving"

    ########
    # BOAT #
    ########

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

    image = fields.Binary(related="boat_id.image")

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
    # CABINS #
    ##########

    cabin_ids = fields.One2many(related="pontoon_id.cabin_ids")

    cabin_ids_invisible = fields.Boolean(compute="compute_cabin_ids_invisible")

    @api.multi
    @api.depends("pontoon_id")
    def compute_cabin_ids_invisible(self):
        """Compute the 'cabin_ids_invisible' field value of some 'cabin'."""
        for record in self:
            record.cabin_ids_invisible = not record.pontoon_id

    #####################################
    # ACTIONS AND OTHER NON ORM METHODS #
    #####################################

    def mass_reserving(self):
        """"""
        context = self.env.context
        if "active_model" in context and context["active_model"] == "sale.order":
            order_id = self.env["sale.order"].browse(context["active_id"])
            template_order_id = self.env["sale.order.template"].search([], limit=1)
            order_id.sale_order_template_id = template_order_id
            order_id.onchange_sale_order_template_id()
