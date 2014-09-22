from openerp.addons.extension_management import extension_management
from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.sql import drop_view_if_exists

class farmer_report(osv.Model):
	_name = 'farmer.report'
	_auto = False
	_rec_name = 'create_date'
	_columns = {
    	'create_date': fields.datetime('Create date', readonly=True),  # TDE FIXME master: rename into date_order
        'name': fields.char('Name', readonly=True),
       	'pin_code': fields.integer('PIN'),	
	}
	_order = 'create_date'
  
  	def init(self, cr):
  		tools.drop_view_if_exists(cr, 'farmer_report')
  		cr.execute("""
            CREATE OR REPLACE VIEW farmer_report AS (
                SELECT
                	id,
                   	c.name as name,
                    c.create_date as create_date,
                    c.pin_code as pin_code
                   
                FROM
                    farmer_detail c
               
            )""")


farmer_report()
	


	