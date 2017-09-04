# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
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
###############################################################################

from openerp import api, models


class DeliverySlipReport(models.AbstractModel):
    _name = 'report.stock.report_deliveryslip'

    @api.multi
    def render_html(self, data=None):
        Report = self.env['report']
        report = Report._get_report_from_name(
            'stock.report_deliveryslip')
        StockWarehouseReturn = self.env['stock.warehouse.return']
        warehouse_returns = StockWarehouseReturn.search([])
        data['extra_data'] = {
            'warehouse_returns': warehouse_returns,
            }
        StockPicking = self.env['stock.picking']
        docs = StockPicking.browse(self._ids)
        import logging
        _logger = logging.getLogger(__name__)
        _logger.debug('DEBUG REPORT DELIVERY DOCS %s', self)
        _logger.debug('DEBUG REPORT DELIVERY DOCS ids %s', self._ids)
        _logger.debug('DEBUG REPORT DELIVERY MODEL %s', report.model)
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': docs,
            'data': data['extra_data'],
        }

        return Report.render('stock.report_deliveryslip', docargs)
