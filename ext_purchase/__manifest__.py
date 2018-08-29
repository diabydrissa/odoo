# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Gestion des achats',
    'version': '1.1',
    'author': 'COULIBALY KONZAGA APOLLINAIRE',
    'category': 'Achats',
    'summary': 'Purchase Orders, Receipts, Vendor Bills',
    'description': "",
    'website': 'https://www.odoo.com/page/purchase',
    'depends': ['base','purchase'],
    'data': [
        'views/res_partner.xml',
        #'views/menu.xml',
        #'views/section_view.xml','views/village_view.xml',
        #'views/purchase_order.xml',
        #'report/demande_de_prix.xml',
    ],
}