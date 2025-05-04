from email.policy import default

from dateutil.utils import today
from datetime import date, timedelta
from odoo import fields, models
from odoo.tools import start_of


class Property(models.Model):
    _name = "estate.property"
    _description = "This is the real estate modul"

    type_id = fields.Many2one("estate.property.type", string="Property Type")
    tag_id = fields.Many2many(comodel_name="estate.property.tags", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    data_availability = fields.Date(
        string="Availability Date",
        default=lambda self: date.today() + timedelta(days=30),
    )

    expected_price = fields.Float(string="Expected price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [
            ("North", "north"),
            ("West", "west"),
            ("South", "south"),
            ("East", "east"),
        ],
        default="North",
    )
