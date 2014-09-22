from openerp.osv import fields, osv
class extension_management(osv.Model):
	_name = "extension.management"
	_description = "Extension Management"

	_columns = {
		'extension_name' : fields.char('Extension Name'),
		'farmer_line':fields.one2many('farmer.detail', 'farmer'),
		'farmer_id' : fields.many2one('farmer.detail', 'Farmer Name'),
		'meeting_line' : fields.one2many('farmer.meeting','meeting'),
		'worker_name' : fields.many2one('hr.employee','Extension Worker'),
	}
extension_management()

class farmer_detail(osv.Model):
	_name = "farmer.detail"
	_description = "Farmer Detail"
	_columns = {
		'farmer' : fields.many2one('extension.management', readonly=True),
		'farmer1' : fields.many2one('farmer.meeting', readonly=True),
		'farm_line':fields.one2many('plot', 'farm'),
		'equipment_line' : fields.one2many('equipment.detail','equipment'),
		'livestock_line' : fields.one2many('livestock.detail','cattle'),
		'meeting_line' : fields.one2many('farmer.meeting','meeting'),
		'image': fields.binary("Photo",help="This field holds the image"),
		'name' : fields.char('Name'),
		'phone_number' : fields.integer('Phone Number'),
		'email' : fields.char('Email',size=64),
		'address' : fields.char('Address', size=64),
		'address_home_id': fields.many2one('res.partner', 'Home Address'),
		'date_of_birth' : fields.datetime('Date of Birth',size=64),
		'country_id': fields.many2one('res.country', 'Nationality'),
		'identification_id': fields.char('Identification No'),
		'passport_id': fields.char('Passport No'),
		'gender': fields.selection([('male', 'Male'), ('female', 'Female')], 'Gender'),
        'marital': fields.selection([('single', 'Single'), ('married', 'Married'), ('widower', 'Widower'), ('divorced', 'Divorced')], 'Marital Status'),
		'bank_account_id': fields.many2one('res.partner.bank', 'Bank Account Number', domain="[('partner_id','=',address_home_id)]", help="Employee bank salary account"),
		'farmer_id' : fields.many2one('farmer.detail', 'Farmer Name'),
		'village' : fields.char('Village Name'),
		'district' : fields.char('District'),
		'state' : fields.char('State'),
		'pin_code' : fields.integer('Pin Code'),
		'taluka' : fields.char('Taluka'),
		'edu_qualification' : fields.char('Qualification',size=64),
		'state':fields.selection([('New','New'),('open','Open'),('confirm','Confirmed'),('cancel','Cancelled')], 'Status', readonly=True, select=True),
	}
	_defaults = {
    	'state': 'New',
    }
 	def print_quotation(self, cr, uid, ids, context=None):
		'''
		This function prints the sales order and mark it as sent, so that we can see more easily the next step of the workflow
		'''
		assert len(ids) == 1, 'This option should only be used for a single id at a time'
		self.signal_workflow(cr, uid, ids, 'quotation_sent')
		return self.pool['report'].get_action(cr, uid, ids, 'extension_management.report_farmer', context=context)


farmer_detail()

class plot(osv.Model):
	_name = "plot"
	_description = "Plot"
	_inherit = 'plot'
	_columns = {
		'farm' : fields.many2one('farmer.detail', readonly=True),
		'plot_id' : fields.many2one('plot', readonly=True),
		'farmer_id' : fields.many2one('farmer.detail','Farmer Name'),
	}
plot()

class farmer_meeting(osv.Model):
	_name = "farmer.meeting"

	_description = "Farmer Meeting"
	_columns = {
		'meeting' : fields.many2one('farmer.detail',readonly=True),
		'subject' : fields.char('Meeting Subject',size=60,help='Subject',required=True),
		'date' : fields.datetime("Meeting Date",size=60,help='Date',required=True),
		'location' : fields.char('Location' ,size=60,help='location', required=True),
		'duration' : fields.integer('Duration' ,size=60,help='Duration', required=True),
		'description' : fields.char('Description',size=60,help="Description"),
		'start_time' : fields.datetime("Starting At",size=60,help='Starting'),
		'end_time' : fields.datetime("End At",size=60),
		'all_day' : fields.boolean("All Day"),
		'meeting_purpose' : fields.char('Meeting Purpose',size=60,required=True),
		'farmer_line':fields.one2many('farmer.detail', 'farmer1'),
		'farmer_id':fields.many2one('farmer.detail', 'Farmer Name'),
	} 
farmer_meeting()

class equipment_detail(osv.Model):
	_name = 'equipment.detail'
	_description = "Equipment Detail"
	_columns = {
		'equipment' : fields.many2one('farmer.detail',readonly=True),
		'equipment_name' : fields.char("Equipment Name"),
		'quantity' : fields.integer('Equipment Quantity'),
	}
equipment_detail()

class livestock_detail(osv.Model):
	_name = 'livestock.detail'
	_description = "Livestock details"
	_columns = {
		"cattle" : fields.many2one("farmer.detail"),
		"cattle_name" : fields.char("Cattle Name"),
		"cattle_qty" : fields.integer("Quantity"),
	}
livestock_detail()
 







