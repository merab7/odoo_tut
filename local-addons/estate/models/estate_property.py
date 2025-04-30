from email.policy import default
from datetime import date, timedelta

from dateutil.utils import today

from odoo import  fields, models
from odoo.odoo.fields import Datetime

Datetime.
class Property(models.Model):
    _name = "estate.property"
    _description = "This is the real estate modul"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    data_availability = fields.Date(string = "Date", copy=False)
    expected_price = fields.Float(string= "Expected price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling price", readonly=True,copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area(sqm)")
    facades  = fields.Integer(string="Facades")
    garage = fields.Boolean(string = "Garage", default=False)
    garden = fields.Boolean(string = "Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'),('east', 'East'), ('west', 'West')], string="garden Orientation", default='north')


