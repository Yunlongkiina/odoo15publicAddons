# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string="name", required=True)
    active = fields.Boolean(string="Active", default=True)
