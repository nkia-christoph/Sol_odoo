# -*- coding: utf-8 -*-
#################################################################################
#
#
#################################################################################

from odoo import api, fields, models, _


class ImportProducts(models.TransientModel):
    _name = 'sol.import.products'
    _description = 'Import Child Products'

    products = fields.Many2many(comodel_name='product.template',
                                domain="[('type', '=', 'service'),('is_root', 'in', ['no'])]")

    @api.multi
    def import_child_products(self):
        product_obj = self.env['product.template']
        root_product = product_obj.browse(self.env.context.get('active_id', False))
        if root_product:
            if self.products:
                root_product.write({
                    'product_child_ids': [(6, 0, self._prepare_child(root_product.product_child_ids, self.products))]
                })
        return {'type': 'ir.actions.act_window_close', }

    def _prepare_child(self, old_child, new_child):
        _intersection = old_child & new_child
        _sub = new_child - old_child
        _union = _sub | _intersection
        return _union.ids
