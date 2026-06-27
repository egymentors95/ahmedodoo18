from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    building_number = fields.Char(string="Building Number")
    unit_number = fields.Char(string="Unit Number")
    additional_no = fields.Char(string="Additional Number")
    cr_no = fields.Char(string="CR Number")
