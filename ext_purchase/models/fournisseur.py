# -*- coding: utf-8 -*-
from odoo import models, fields

class res_partner(models.Model):
 	"""docstring for Gestion_village"""
 	_name = "res.partner"
 	_inherit = "res.partner"
 	_description = "Création des fournisseurs"
 	compte_contribuable = fields.Char("Compte contribuable",required= False)
 	numero_agrement = fields.Char("N° agréement",required= False)
 	code_import_export = fields.Char("Code import-export",required= False)
 	regime_imposition = fields.Char("Regime imposition",required= False)