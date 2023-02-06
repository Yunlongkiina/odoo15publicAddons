# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    # ir.config_parameter will store config parameters
    cancel_days = fields.Integer(
        string='Cancel Days', config_parameter='odoo_learning_hospital_management.cancel_days')
