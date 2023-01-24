# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = "ref"

    patient_id = fields.Many2one('hospital.patient', string="patient")
    gender = fields.Selection(related="patient_id.gender")
    ref = fields.Char(string="Patient Ref")
    appointment_time = fields.Datetime(
        string="Appointment Time", default=fields.Datetime.now)
    booking_time = fields.Date(string="Booking Date")

    @api.onchange('patient_id')
    def onchange_patient_ref(self):
        self.ref = self.patient_id.ref
