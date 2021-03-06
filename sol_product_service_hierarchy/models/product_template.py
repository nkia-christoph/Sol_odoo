# -*- coding: utf-8 -*-
#################################################################################

#################################################################################
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_child_ids = fields.Many2many(comodel_name="product.template",
                                           relation="product_hierarchy_rel",
                                           column1="root_id",
                                           string="Sub Service",
                                           domain="[('type', '=', 'service'),('is_root', 'in', ['no'])]",
                                           copy=False,
                                           help="Add Child.")
    is_shared = fields.Boolean(string="is shared", copy=False,
                                    domain="[('type', '=', 'service')]",
                                    default=False,
                                    help="shared product below to all products.")
    is_auto_inserted = fields.Boolean(string="auto insert product", copy=False,
                             default=False,
                             help=" auto insert product into order when the its parent is add to order line.")
    is_auto_price = fields.Boolean(string="extra price", copy=False,
                                      default=False,
                                      help="include product price in order line price.")
    is_root = fields.Selection(string="Product hierarchy", selection=[('simple', 'is a service'),
                                                            ('root', 'is a root'),
                                                            ('no', 'is a child')],
                               default='simple')
    extra_formatting = fields.Char(string="Formatting",
                                   default="{name}",
                                   help="formatting child in description, possible values: this {name}, has {price}."
                                        "the order doesn't matter")
