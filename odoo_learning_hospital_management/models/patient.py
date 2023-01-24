# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api


class HospitalPaitent(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char()
    ref = fields.Char(string="Reference")
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(
        string="Age", compute="_compute_patient_age", tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, default="female")
    active = fields.Boolean(string="Active", default=True)

    def _compute_patient_age(self):
        for patient in self:
            today = date.today()
            if patient.date_of_birth:
                patient.age = today.year - patient.date_of_birth.year
            else:
                patient.age = 1
