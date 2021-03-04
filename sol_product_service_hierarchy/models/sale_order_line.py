# -*- coding: utf-8 -*-
#################################################################################

#################################################################################

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_template_id = fields.Integer(compute='_compute_product_template', string="product template id")
    products_child_readonly = fields.Boolean(string="Simple Service", copy=False,
                                             default=False,
                                             compute='_compute_products_child_readonly')
    products_child = fields.Many2many('product.template', string='Product child',
                                      domain="['|', '&',('product_child_ids', '=',product_template_id),"
                                             "('type', '=', 'service'),('is_shared', '=', True)]",
                                      help='Product child')

    @api.multi
    @api.depends('product_id')
    def _compute_product_template(self):
        for line in self:
            line.product_template_id = line.product_id.product_tmpl_id.id

    @api.multi
    @api.depends('product_id')
    def _compute_products_child_readonly(self):
        for line in self:
            line.products_child_readonly= (line.product_id.is_root in ['simple','no']) \
                                          or (line.product_id.type in ['consu','product'])

    @api.onchange('products_child')
    def _onchange_products_child(self):
        if self.products_child:
            # *self.product_uom_qty
            sum_price = self.price_unit
            product_names = self.product_id.name
            for rec in self.products_child:
                extra_formatting = rec.extra_formatting or '{name}'
                product_names += '\r\n' + extra_formatting.format(name=rec.name, price=rec.list_price)
                if rec.is_auto_price:
                    sum_price = sum_price + rec.list_price

            self.name = product_names
            self.price_unit = sum_price
        else:
            self.name = self.product_id.name
            self.price_unit = self.product_id.list_price

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        if not self.product_uom or not self.product_id:
            self.price_unit = 0.0
            return
        if self.order_id.pricelist_id and self.order_id.partner_id:
            sum_extra_price = 0.0
            for rec in self.products_child:
                if rec.is_auto_price:
                    product = rec.with_context(
                        lang=self.order_id.partner_id.lang,
                        partner=self.order_id.partner_id,
                        quantity=self.product_uom_qty,
                        date=self.order_id.date_order,
                        pricelist=self.order_id.pricelist_id.id,
                        uom=self.product_uom.id,
                        fiscal_position=self.env.context.get('fiscal_position'))
                    product_price = self.env['account.tax']._fix_tax_included_price_company(
                        self._get_display_price(product),
                        product.taxes_id, self.tax_id,
                        self.company_id)
                    sum_extra_price = sum_extra_price + product_price

            self.price_unit = self.price_unit + sum_extra_price

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            if self.product_id.type == 'service' and self.product_id.is_root != 'simple':
                product_object = self.env['product.template'] \
                    .search(['&', '|',
                             ('id', 'in', self.product_id.product_child_ids.ids),
                             ('is_shared', '=', True), ('is_auto_inserted', '=', True)])
                self.products_child = [(6, 0, product_object.mapped('id'))]
