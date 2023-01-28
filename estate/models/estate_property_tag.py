# -*- coding: utf-8 -*-

from odoo import fields, models, api
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


class EstatePropertyType(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Name", required=True)
    color = fields.Integer("Color Index")


""" # Relational (for inline view)
    property_ids = fields.One2many(
        "estate.property", "tag_ids", string="Properties")

    def testfunc(self):
        for record in self.property_ids:
            _logger.debug(" from property tags ")
            _logger.debug(record)
 """
