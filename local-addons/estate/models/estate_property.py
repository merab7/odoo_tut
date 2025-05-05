from datetime import date, timedelta
from odoo import fields, models, api


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

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    total_area = fields.Integer(string="Total Area", compute="_compute_total_area")
    garden_orientation = fields.Selection(
        [
            ("North", "north"),
            ("West", "west"),
            ("South", "south"),
            ("East", "east"),
        ],
        default="North",
    )
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one("res.partner", string="Buyer")




