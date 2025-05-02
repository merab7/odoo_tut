from odoo import fields, models


class Student(models.Model):

    _name = "wb.students"
    _description = "this is students module"

    name = fields.Char(string="name")
    name1 = fields.Char(string="name1")
    name2 = fields.Char(string="name2")
    name3 = fields.Char(string="name3")
    name4 = fields.Char(string="name4")
