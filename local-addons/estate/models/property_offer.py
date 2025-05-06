from datetime import timedelta, datetime
from odoo import models, fields, api


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

    name = fields.Char(string="Description", compute='_compute_name')
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property")
    offer_name = fields.Char(string="Offer Name", required=True)
    offer_price = fields.Float(string="Offer Price", required=True)
    offer_status = fields.Char(string="Offer Status",  compute='_compute_offer_status')
    validity = fields.Integer(string="Validity")
    creation_date = fields.Date(string="Creation Date", default=fields.Date.today())
    deadline = fields.Date(string="Deadline",
                           compute="_compute_deadline",
                           inverse="_inverse_deadline",
                           default=fields.Date.today())





    _sql_constraints = [
        ('check_validity', 'CHECK(validity >= 0)', 'Validity cannot be negative')
    ]



    def _inverse_deadline(self):
        for record in self:
            if record.deadline and record.creation_date:
                record.validity = (record.deadline - record.creation_date).days
            else:
                record.validity = False

    @api.depends('deadline')
    def _compute_offer_status(self):
        today_date = datetime.today().date()
        for record in self:
            if not record.deadline:
                record.offer_status = 'active'
            elif today_date > record.deadline:
                record.offer_status = 'expired'
            else:
                record.offer_status = 'active'


    # #so what this cron job with this autovacuum decorator does is that it will run this function every day and aplay
    # #function under it in our case it is unlinking offers that are expired.
    # @api.autovacuum
    # def _clean_offers(self):
    #     self.search(['offer_status', '=', 'expired']).unlink()



    @api.depends("creation_date", "validity")
    def _compute_deadline(self):
        for record in self:
            if record.validity:
                record.deadline = record.creation_date + timedelta(days=record.validity)
            else:
                record.deadline = False



    @api.depends("property_id","partner_id")
    def _compute_name(self):
        for record in self:
            if record.partner_id and record.property_id:
                record.name = f"{record.partner_id.name} - {record.property_id.name}"
            else:
                record.name = False



