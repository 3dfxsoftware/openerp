#this is the name of the module

from openerp.osv import fields, osv

class sale_subject(osv.osv):
    
    _inherit = "sale.order"
    
    _columns = {
                'sale_subject':fields.char('Sale Subject', size=64, required = True)
                }
    
    _defaults = {
                 'sale_subject': " "
                 }
    
sale_subject()