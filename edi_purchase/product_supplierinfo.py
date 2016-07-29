# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Akretion (<http://www.akretion.com>).
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

from openerp.osv.orm import Model
from openerp.osv import fields, orm


class ProductSupplierinfo(Model):
    _inherit = 'product.supplierinfo'


    def _get_edi_file_format(self, cr, uid, context=None):
        return [
            ('csv', 'CSV'),
            ('xls', 'Excel'),
        ]

    _columns = {
        'purchase_edi_id': fields.many2one(
            'purchase.edi.profile',
            'Edi Profile'),
    }
