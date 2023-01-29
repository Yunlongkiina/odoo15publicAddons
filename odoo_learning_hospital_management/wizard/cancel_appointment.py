# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime

# import the library
import logging
# get the logging object
_logger = logging.getLogger(__name__)
# set up the log level
_logger.setLevel(logging.DEBUG)
# appending mode 'a', utf-8 encoding is set up to prevent messy codes
test_log = logging.FileHandler(
    '../odoo-debug/odoo-debug.log', 'a', 'utf-8')
# the log level output to files
test_log.setLevel(logging.DEBUG)
# the log format output to files
formatter = logging.Formatter(
    '%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s - %(process)s')
test_log.setFormatter(formatter)
# load files into the logger object
_logger.addHandler(test_log)


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


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    @api.model
    def default_get(self, fields):
        #print(bcolors.WARNING + str(values) + bcolors.ENDC)
        # _logger.debug(fields)
        # _logger.debug(bcolors.WARNING + str(dir(self)) + bcolors.ENDC)
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['cancel_date'] = datetime.date.today()
        return res

    appointment_id = fields.Many2one(
        'hospital.appointment', string="Appointment")
    cancel_reason = fields.Text(string="Reason")
    cancel_date = fields.Date(
        sting="Cancellation Date")

    def action_cancel(self):
        return
