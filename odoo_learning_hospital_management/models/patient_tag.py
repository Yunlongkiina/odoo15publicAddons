# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    color_dynamic = fields.Char(string="Dynamic Color")

    _sql_constraints = [
        ('patient_tag_uniq', 'unique (name)',
         'The tag of the patient must be unique!'),
    ]
