# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class HospitalPaitent(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char()
    ref = fields.Char(string="Reference")
    patient_email = fields.Char(string="Patient Email")
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(
        string="Age", compute="_compute_patient_age", tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, default="female")
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one(
        'hospital.appointment', string="Appointment")
    image = fields.Image(string="Image")
    patient_sign = fields.Binary(string="Patient sign")
    tag_ids = fields.Many2many('patient.tag', string="Patient Tags")
    appointment_count = fields.Integer(
        string="Appointment Count", compute="_compute_appountment_count")
    appointment_ids = fields.One2many(
        'hospital.appointment', 'patient_id', string="Appointment")

    @api.depends('appointment_ids')
    def _compute_appountment_count(self):
        for record in self:
            record.appointment_count = self.env['hospital.appointment'].search_count(
                [('patient_id', '=', record.id)])

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth > fields.Date.today():
                raise ValidationError(
                    _('The date of birth you entered is not allowed!'))
        return

    # overwrite create method
    @api.model
    def create(self, values):
        #print(bcolors.WARNING + str(values) + bcolors.ENDC)
        if not values['ref']:
            values['ref'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient')
        return super(HospitalPaitent, self).create(values)

    # overwrite write method
    # write mdethod does not need @api.model
    def write(self, values):
        #print(bcolors.WARNING + str(type(values)) + bcolors.ENDC)
        if 'ref' in values:
            if not values.get('ref') and not values['ref']:
                values['ref'] = self.env['ir.sequence'].next_by_code(
                    'hospital.patient')

        #print(bcolors.WARNING + str(values) + bcolors.ENDC)
        return super(HospitalPaitent, self).write(values)

    def _compute_patient_age(self):
        for patient in self:
            today = date.today()
            if patient.date_of_birth:
                patient.age = today.year - patient.date_of_birth.year
            else:
                patient.age = 1
