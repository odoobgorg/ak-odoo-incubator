# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Akretion (<http://www.akretion.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{'name': 'Stock Orderpoint Specific Location',
 'version': '0.1',
 'author': 'Akretion,Odoo Community Association (OCA)',
 'website': 'http://www.akretion.com',
 'description': """
    Allow to create reception in a sublocation of the location's orderpoint
    Warning : need to patch Odoo purchase module to make it work.
    https://github.com/akretion/odoo/tree/9.0-hooks
 """,
 'license': 'AGPL-3',
 'category': 'Generic Modules/Others',
 'summary': 'Export',
 'depends': ['stock',
             'purchase'
             ],
 'data': [
      'views/stock_orderpoint_view.xml',
      'views/purchase_order_view.xml',
 ],
 'installable': True,
 }
