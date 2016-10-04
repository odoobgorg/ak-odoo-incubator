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

from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    edi_transfer_method = fields.Selection(
        selection=[('mail', 'E-mail'),
                   ('external_location', 'SFTP/FTP')],
        string='Edi Transfer Method')
    edi_external_location_id = fields.Many2one(
            'external.file.location',
            string='FTP/SFTP Location')
    edi_mail_template_id = fields.Many2one(
            'mail.template',
            string='Edi Mail Template')
    edi_empty_file = fields.Boolean('Send EDI empty file')

