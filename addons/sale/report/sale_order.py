# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
import time

from openerp.report import report_sxw
from num2word import to_card

class order(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(order, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time, 
            'show_discount':self._show_discount,
            'card':self.card,
            'new':self.new,
        })
    
    def _show_discount(self, uid, context=None):
        cr = self.cr
        try: 
            group_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'sale', 'group_discount_per_so_line')[1]
        except:
            return False
        return group_id in [x.id for x in self.pool.get('res.users').browse(cr, uid, uid, context=context).groups_id]

    def card(self, res, curr_obj):
        print res
#         new = ''
#         for i in res:
#             try:
#                 new = new + str(int(i))
#             except ValueError as e:
#                 if i == '.':
#                     new = new + i
# #                 if i == '$':
# #                     tag = 'USD'
#                 print e
#         res = float(res)
        print curr_obj
        res = to_card(res)
        res = res.title()
        res = res.replace(" And ", " and ")
        print res
        return res
    
    def new(self, date):
        date = date.replace( "/", "-")
        year, month, day = date.split("-")
        format = ''
        format = format + day + month + year
        return format

report_sxw.report_sxw('report.sale.order', 'sale.order', 'addons/sale/report/sale_order.rml', parser=order, header="external")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

