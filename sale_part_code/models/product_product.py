# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductProduct(models.Model):
    """Inherited Product variant for adding sale part code."""
    _inherit = 'product.product'

    sale_part_code = fields.Char(string='Sale Part Code',
                                 help='Unique code for Product.')
    _sql_constraints = [
        ('sale_part_code', 'UNIQUE(sale_part_code)',
         'The Sale Part Code must be unique')]

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100,
                     order=None):
        """Allows to search the Product based on the field sale_part_code"""
        args = list(args or [])
        if name:
            args += [('sale_part_code', operator, name)]
            return self._search(args, limit=limit, order=order)