from odoo import models, fields


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property")
    offer_name = fields.Char(string="Offer Name", required=True)
    offer_price = fields.Float(string="Offer Price", required=True)
    offer_status = fields.Selection(
        [("active", "Active"), ("expired", "Expired")], string="Offer Status"
    )
