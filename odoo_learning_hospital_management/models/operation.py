from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalOperation(models.Model):
    _name = 'hospital.operation'
    _description = 'Hospital Operation'
    _log_access = False

    doctor_id = fields.Many2one('res.users', string='Doctor')
    operation_name = fields.Char(string='Name')
    # Reference Field In Odoo
    reference_record = fields.Reference(selection=[(
        'hospital.patient', 'patient'), ('hospital.appointment', 'Appointment')], string="Record")

    @api.model
    def name_create(self, name):
        return self.create({'operation_name': name}).name_get()[0]
