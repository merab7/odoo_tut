from datetime import timedelta
from odoo import models, fields, api


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
    validity = fields.Integer(string="Validity")
    creation_date = fields.Date(string="Creation Date", default=fields.Date.today())

    @api.depends("creation_date", "validity")
    def _compute_deadline(self):
        for record in self:
            if record.validity:
                record.deadline = record.creation_date + timedelta(days=record.validity)
            else:
                record.deadline = False

    def _inverse_deadline(self):
        for record in self:
                record.validity = (record.deadline - record.creation_date).days




    deadline = fields.Date(string="Deadline", compute="_compute_deadline",  inverse="_inverse_deadline")

