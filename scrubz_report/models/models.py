from odoo import models, fields


class SaleExtInh(models.Model):
    _inherit = 'sale.order'

    subject = fields.Char(string='Subject')
