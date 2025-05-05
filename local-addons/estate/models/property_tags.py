from odoo import models, fields


class PropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Property Tags"

    name = fields.Char(string="Tag Name", required=True)
