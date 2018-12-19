# -*- coding: utf-8 -*-
####################   TOP1 CI      ####################
#    TOP1 CI. Ltd.
#    Copyright (C) 2010-TODAY TOP1 CI(<http://www.top1ci.com>).
#    Author: Farooq Arif(<http://www.top1ci.com>)
#
#    It is forbidden to distribute, or sell copies of the module.
#
#    License:  OPL-1
####################   TOP1 CI      ####################
#
#   Send and email at features@aarsol.com  after download, so about latest updates on this module, you will be informed
#
#
{
    'name': 'Point de vente code barre',
    'version': '10.7',
    'description': """POS Receipt with Barcode and Logo""",
    'author': 'Diaby Top1 africa',
    'company': 'TOP1 CI Limited.',
    'website': 'http://www.top1ci.com',
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale'],
    'license': 'OPL-1',
    'data': [
    	'views/import.xml', 
    	'views/pos_order.xml',    	
    ],
    'qweb': ['static/src/xml/posticket.xml'],
    'images': ['static/description/banner.png'],
    'demo': [],        
    'installable': True,
    'application': True,
    'auto_install': False,

}
