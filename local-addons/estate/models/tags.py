from odoo import models, fields
from odoo.addons.im_livechat.tools.misc import force_guest_env


class PropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Property Tags"

    name = fields.Char(string="Tag Name", required=True)
