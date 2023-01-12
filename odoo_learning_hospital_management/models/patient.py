# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPaitent(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char()
    ref = fields.Char(string="Reference")
    age = fields.Integer()
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string='Gender')
    active = fields.Boolean(string="Active", default=True)
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
