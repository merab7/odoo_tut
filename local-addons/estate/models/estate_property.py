from email.policy import default


from odoo import  fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "This is the real estate modul"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    data_availability = fields.Date(string="Date")
    expected_price = fields.Float(string="Expected price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")

