# -*- coding: utf-8 -*-
from odoo import api, models, fields

class PurchaseOrderLine(models.Model):
	"""docstring for purchaseOrder"""
	_name = "purchase.order.line"
	_inherit = "purchase.order.line"
	_description = "Montant du Transport"
	tp = fields.Monetary(string='Transport', required= False)
	#price_subtotal = 

	# @api.depends('product_qty', 'price_unit', 'taxes_id','tp')
	# def _compute_amount(self):
	# 	for line in self:
	# 		taxes = line.taxes_id.compute_all(line.price_unit, line.order_id.currency_id, line.product_qty, line.tp, product=line.product_id, partner=line.order_id.partner_id)
	# 		line.update({
	# 			'price_subtotal': taxes['total_excluded'],
	# 			'price_total': taxes['total_included'],
	# 			'price_subtotal': taxes['total_excluded'],
	# 			})