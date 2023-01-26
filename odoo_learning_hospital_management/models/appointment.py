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
    booking_Date = fields.Date(string="Booking Date")
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

    doctor_id = fields.Many2one('res.users', string="Doctor")
    # pharmacy_line_ids will create many lines,
    # same idea as sales order line
    # The model hospital.pharmacy.line need to declare
    # corresponding Many2one field
    pharmacy_line_ids = fields.One2many(
        'hospital.pharmacy.line', 'appointment_id', string="Pharmacy Line")

    hide_sale_price = fields.Boolean(string="Hide Sale Price")

    @api.onchange('patient_id')
    def onchange_patient_ref(self):
        self.ref = self.patient_id.ref

    def test_action(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Congraduations! Hope you recover soon!',
                'type': 'rainbow_man'
            }
        }

    def action_in_consultiation(self):
        self.state = 'in_consultiation'

    def action_done(self):
        self.state = 'done'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Oh yeah!!!!!!!!!!!!!!!!!!',
                'type': 'rainbow_man'
            }
        }

    def action_cencel(self):
        self.state = 'cancel'


class AppointmentPharmacyLines(models.Model):
    _name = 'hospital.pharmacy.line'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one('product.product')
    price_unit = fields.Float(string="Sale price")
    quantity = fields.Integer(string="Quantity")
    #
    appointment_id = fields.Many2one(
        'hospital.appointment', string="Appointment")
