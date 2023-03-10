from dateutil.relativedelta import relativedelta
from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class EstatePropertyOffer(models.Model):
    # --Private Attributes--
    _name = "estate.property.offer"
    _description = "estate property offer model"
    _order = "price desc"
    # --Field Declaration--
    # Basic
    price = fields.Float('Price', required=True)
    validity = fields.Integer(string="validity days", default=7)
# Special
    state = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        string="Status",
        copy=False,
        default=False,
    )

    partner_id = fields.Many2one(
        'res.partner', string="Partner", required=True)
    property_id = fields.Many2one(
        "estate.property", string="Property", required=True)
# Computed
    date_deadline = fields.Date(
        string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
# ---------------------------------------- Compute methods ------------------------------------

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days

  # ---------------------------------------- Button Actions ------------------------------------
    def action_accept(self):
        if "accepted" in self.mapped("property_id.offer_ids.state"):
            raise UserError("An offer is already been accepted!")
        self.write(
            {
                "state": "accepted"
            }
        )
        return self.mapped("property_id").write(
            {
                "state": "offer_accepted",
                "selling_price": self.price,
                "buyer_id": self.partner_id.id,
            }
        )

    def action_refuse(self):
        return self.write({
            "state": "refused"
        })
