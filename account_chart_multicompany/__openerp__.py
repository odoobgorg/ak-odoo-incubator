# coding: utf-8
##############################################################################
#
#    Copyright (C) 2016 AKRETION (<http://www.akretion.com>).
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


{
    'name': 'Account Chart MultiCompany',
    'version': '8.0.0.1.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """""",
    'author': 'Akretion, Odoo Community Association (OCA)',
    'website': 'http://www.akretion.com',
    'depends': [
        'account',
        'base',
        'base_suspend_security',
    ],
    'data': ['account_view.xml',
             'security/account_security.xml',
             'security/ir.rule.csv',
            ],
    'installable': True,
}