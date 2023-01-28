# -*- coding: utf-8 -*-

from odoo import models, fields, api
from pprint import pformat
# # import the library
# import logging
# # get the logging object
# _logger = logging.getLogger(__name__)
# # set up the log level
# _logger.setLevel(logging.DEBUG)
# # appending mode 'a', utf-8 encoding is set up to prevent messy codes
# test_log = logging.FileHandler(
#     '../odoo-debug/odoo-debug.log', 'a', 'utf-8')
# # the log level output to files
# test_log.setLevel(logging.DEBUG)
# # the log format output to files
# formatter = logging.Formatter(
#     '%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s - %(process)s')
# test_log.setFormatter(formatter)
# # load files into the logger object
# _logger.addHandler(test_log)


class odoo_front_test(models.Model):
    _name = 'odoo_front_test.odoo_front_test'
    _description = 'odoo_front_test.odoo_front_test'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            # _logger.debug(pformat(dir(record)))
            record.value2 = float(record.value) / 100

    testYunlong = "test one"

    def testOddoFuc(self):
        testYunlong = "test two"
        return testYunlong
    # _logger.debug(testYunlong)
