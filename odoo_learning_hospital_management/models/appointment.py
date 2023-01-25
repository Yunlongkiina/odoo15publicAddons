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
    # this is a Html field, which is allow you to write many things
    #
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultiation', 'In_consultiation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], string="Status", default="draft", required=True)

    @api.onchange('patient_id')
    def onchange_patient_ref(self):
        self.ref = self.patient_id.ref

    def test_action(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Oh yeah!!!!!!!!!!!!!!!!!!',
                'type': 'rainbow_man'
            }
        }
