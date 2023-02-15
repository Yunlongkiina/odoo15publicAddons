# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from dateutil import relativedelta


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
        string="Age", compute="_compute_patient_age", search="_search_age", tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, default="female")
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one(
        'hospital.appointment', string="Appointment")
    image = fields.Image(string="Image")
    patient_sign = fields.Binary(string="Patient sign")
    tag_ids = fields.Many2many('patient.tag', string="Patient Tags")
    appointment_count = fields.Integer(
        string="Appointment Count", compute="_compute_appointment_count")
    appointment_ids = fields.One2many(
        'hospital.appointment', 'patient_id', string="Appointment")
    parent = fields.Char(string="Parent")
    marital_status = fields.Selection(
        [('married', 'Married'), ('single', 'Single')], string="Marital Status", tracking=True)
    partner_name = fields.Char(string="Partner Name")
    is_birth = fields.Boolean(
        string="Birthday ?", compute="_compute_is_birthday")
    phone = fields.Char(string="Phone")
    e_mail = fields.Char(string="E_mail")
    website = fields.Char(string="Website")

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for record in self:
            appointment_group = self.env['hospital.appointment'].read_group(
                domain=[], fields=['patient_id', ], groupby=['patient_id'])
            for appointment in appointment_group:
                patient_id = appointment.get('patient_id')
                patient_record = self.browse(patient_id)
                patient_record.appointment_count = appointment['patient_id_count']
                # get original self
                self -= patient_record
            self.appointment_count = 0

            # second method to get appointment count
            # record.appointment_count = self.env['hospital.appointment'].search_count(
            #     [('patient_id', '=', record.id)])

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth > fields.Date.today():
                raise ValidationError(
                    _('The date of birth you entered is not allowed!'))
        return

    @api.ondelete(at_uninstall=False)
    def _check_appointments(self):
        for record in self:
            if record.appointment_ids:
                raise ValidationError(
                    _('You can not delete a patient has appoints!')
                )
    # overwrite create method

    @api.model
    def create(self, values):
        #print(bcolors.WARNING + str(values) + bcolors.ENDC)
        # if not values['ref']:
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
        return super(HospitalPaitent, self).write(values)

    @api.depends('date_of_birth')
    def _compute_patient_age(self):
        for patient in self:
            today = date.today()
            if patient.date_of_birth:
                patient.age = today.year - patient.date_of_birth.year
            else:
                patient.age = 1

# BUG, need to fix
    # As default compute field is read-only
    # If you need to make a manual entry on compute field, that can be done by giving inverse function.
    # So it triggers call of the decorated function when the field is written/”created”.
    # It reverses the computation and set the relevant fields.
    # @api.depends('age')
    # def _inverse_compute_patient_age(self):
    #     today = date.today()
    #     for record in self:
    #         if record.age:
    #             record.date_of_birth = today - \
    #                 relativedelta.relativedelta(years=record.age)
    #         pass

    def _search_age(self, operator, value):
        searched_date_of_birth = date.today() - relativedelta.relativedelta(years=value)
        start_of_year = searched_date_of_birth.replace(day=1, month=1)
        end_of_year = searched_date_of_birth.replace(day=31, month=12)
        return [('date_of_birth', '>=', start_of_year), ('date_of_birth', '<=', end_of_year)]

    @api.depends('date_of_birth')
    def _compute_is_birthday(self):
        for record in self:
            is_birth = False
            if record.date_of_birth:
                today = date.today()
                if today.day == record.date_of_birth.day and today.month == record.date_of_birth.month:
                    is_birth = True
            record.is_birth = is_birth
