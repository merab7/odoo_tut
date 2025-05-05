from datetime import timedelta, datetime
from odoo import models, fields, api




class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property")
    offer_name = fields.Char(string="Offer Name", required=True)
    offer_price = fields.Float(string="Offer Price", required=True)
    offer_status = fields.Char(string="Offer Status",  compute='_compute_offer_status')





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
            if record.deadline and record.creation_date:
                record.validity = (record.deadline - record.creation_date).days
            else:
                record.validity = False

    deadline = fields.Date(string="Deadline", compute="_compute_deadline", inverse="_inverse_deadline",
                           default=fields.Date.today())

    _sql_constraints = [
        ('check_validity', 'CHECK(validity >= 0)', 'Validity cannot be negative')
    ]

    @api.depends('deadline')
    def _compute_offer_status(self):
        today_date = datetime.today().date()
        for record in self:
            if not record.deadline:
                record.offer_status = 'active'  # or whatever default status you prefer
            elif today_date > record.deadline:
                record.offer_status = 'expired'
            else:
                record.offer_status = 'active'


    #so what this cron job with this autovacuum decorator does is that it will run this function every day and aplay
    #function under it in our case it is unlinking offers that are expired.
    @api.autovacuum
    def _clean_offers(self):
        self.search(['offer_status', '=', 'expired']).unlink()

    # @api.constrains('deadline')
    # def _check_deadline(self):
    #     for record in self:
    #             if record.deadline <= record.creation_date:
    #                 raise models.ValidationError("Deadline cannot be before creation date")

    #so above constrains is validation during the entering the data but it is not validation on the sql level
    #what i mean by that if we have at this point bad data in the database it will now be changed so we can create database constrain


