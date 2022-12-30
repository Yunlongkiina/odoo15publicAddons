#import string
from dateutil.relativedelta import relativedelta
from email.policy import default
from odoo import fields, models, api
from pprint import pformat
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

# import the library
import logging
# get the logging object
_logger = logging.getLogger(__name__)
# set up the log level
_logger.setLevel(logging.DEBUG)
# appending mode 'a', utf-8 encoding is set up to prevent messy codes
test_log = logging.FileHandler(
    '../odoo-debug/odoo-debug.log', 'a', 'utf-8')
# the log level output to files
test_log.setLevel(logging.DEBUG)
# the log format output to files
formatter = logging.Formatter(
    '%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s - %(process)s')
test_log.setFormatter(formatter)
# load files into the logger object
_logger.addHandler(test_log)


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property model"
    _order = "id desc"
    _sql_constraints = [
        ("check_expected_price", "CHECK (expected_price > 0)",
         "The expected price must be strictly positive"),
        ("check_selling_price", "CHECK (selling_price >= 0)",
         "The offer price must be positive"),
    ]

    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)

# ---------------------------------------- Basic ------------------------------------
    name = fields.Char(default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        default=lambda self: self._default_date_availability(), copy=False)
    expected_price = fields.Float(default=100000.00)
    selling_price = fields.Float(default=0)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(default=10)
    facades = fields.Integer('facades')
    garage = fields.Boolean('garage')
    garden = fields.Boolean('garden')
    garden_area = fields.Integer('Garden Area(sqm)')
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('West', 'west'), ('North', 'north'),
                   ('South', 'south'), ('East', 'east')],
        help="Type is used to ")
# ---------------------------------------- Special ------------------------------------

    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )
    active = fields.Boolean("Active", default=True)
    best_price = fields.Float(
        "Best Offer", compute="_compute_best_price", help="Best offer received")

# ---------------------------------------- Relationals ------------------------------------

    # relate property
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    # relate partner
    buyer_id = fields.Many2one(
        'res.partner', string='Buyer', readonly=True, copy=False)
    # relate users
    user_id = fields.Many2one(
        'res.users', string='salesman', default=lambda self: self.env.user)
    # relate estate.property.tag
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    # relate estate.property.offer
    offer_ids = fields.One2many(
        "estate.property.offer", "property_id", string="Offers")
    # _logger.debug(pformat(type(property_type_id)))

    total_area = fields.Float(
        "Total Area (sqm)",
        compute="_compute_total_area",
        help="Total area computed by summing the living area and the garden area"
    )
    best_price = fields.Float(
        "The best price",
        compute="_compute_best_price",
        help="The best price received until now"
    )

  # ---------------------------------------- Compute methods ------------------------------------

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for prope in self:
            prope.best_price = max(prope.offer_ids.mapped(
                'price')) if prope.offer_ids else 0.00

# ---------------------------------------Onchanges --------------------------------
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'East'
        else:
            self.garden_area = 0
            self.garden_orientation = False

# ---------------------------------------- Constrains --------------------------------
    @api.constrains("expected_price", "selling_price")
    def _check_price_difference(self):
        for prop in self:
            if (
                not float_is_zero(prop.selling_price, precision_rounding=0.01)
                and float_compare(prop.selling_price, prop.expected_price * 90.0 / 100.0, precision_rounding=0.01) < 0
            ):
                raise ValidationError(
                    "The selling price must be at least 90% of the expected price! "
                    + "You must reduce the expected price if you want to accept this offer."
                )
# ---------------------------------------- Button Actions ------------------------------------

#    def set_property_as_sold(self):
#        if "canceled" in self.mapped("state"):
#            raise UserError("canceled property cant be sold.")
#        return self.write({"state": "sold"})

    def action_sold(self):
        if "canceled" in self.mapped("state"):
            raise UserError("Canceled properties cannot be sold.")
        return self.write({"state": "sold"})

    def set_property_as_cancelled(self):
        if "sold" in self.mapped("state"):
            raise UserError("sold property cant be canceled")
        return self.write({"state": "canceled"})

# ---------------------------------------- CRUD Methods ------------------------------------
    def unlink(self):
        # if not subset of {"new", "canceled"}
        # _logger.debug(set(self.mapped("state")))
        if not set(self.mapped("state")) <= {"new", "canceled"}:
            raise UserError("Only new and canceled properties can be deleted.")
        return super().unlink()
