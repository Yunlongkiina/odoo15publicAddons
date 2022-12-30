# -*- coding: utf-8 -*-
import json
from odoo import http, fields

from pprint import pformat
from datetime import datetime
from odoo.tools import date_utils
# from collections import defaultdict

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


class OdooFrontTest(http.Controller):
    @http.route('/odoo_front_test/update', auth='public', website=False, csrf=False, type='json', method=['POST'])
    def index(self, **kw):
        _logger.debug(kw)
        return {
            'success': True,
            'status': 'OK',
            'code': 200
        }

    @http.route('/odoo_front_test/odoo_front_test/objects', auth='public')
    def list(self, **kw):
        # _logger.debug(dir(self))
        return http.request.render('odoo_front_test.listing', {
            'root': '/odoo_front_test/odoo_front_test',
            'objects': http.request.env['odoo_front_test.odoo_front_test'].search([]),
        })

    @http.route('/odoo_front_test/odoo_front_test/objects/<model("odoo_front_test.odoo_front_test"):obj>', auth='public')
    def object(self, obj, **kw):
        # _logger.debug(dir(self))
        return http.request.render('odoo_front_test.object', {
            'object': obj
        })

    @http.route('/salesdata/', type='http', auth='public', website='True', method=['GET'])
    def sale_data(self, **post):
        today = fields.Datetime.now()
        tomorrow = date_utils.add(today, days=1)
        # Convert date type from datetime.date type into string
        # d1 = datetime.strftime(tomorrow, "%Y-%m-%d %H:%M:%S")
        tomorrowStr = datetime.strftime(tomorrow, "%Y-%m-%d 23:59:59")
        # last second of today
        todayStr = datetime.strftime(today, "%Y-%m-%d 23:59:59")
        sales_data = http.request.env['sale.order'].sudo().search(
            ['&', ('state', 'in', ['sale', 'sent', 'draft']), ('commitment_date', '>', todayStr), ('commitment_date', '<=', tomorrowStr), ("x_driver_cus", "=", "d1")])

#        sales_order_line = http.request.env['sale.order.line'].sudo().search([
#        ])

        lineArray = []
        testObj = {}
        resultToShow = []
        for order in sales_data:
            for line in order.order_line:
                if line.product_id.x_picking_code == 'FZ':
                    lineArray.append({
                        'name': line.name,
                        'pickingCode': line.product_id.x_picking_code,
                        'qty': line.product_uom_qty,
                    })

        for lineObj in lineArray:
            if lineObj['name'] in testObj.keys():
                testObj[lineObj['name']]['qty'] = int(lineObj['qty']) + \
                    testObj[lineObj['name']]['qty']
            else:
                lineObj['qty'] = int(lineObj['qty'])
                testObj.update(
                    {
                        lineObj['name']: lineObj
                    }
                )

        for value in testObj.values():
            resultToShow.append(value)

        values = {
            'records': sales_data,
            'salesOrderLines': resultToShow,
        }
        return http.request.render('odoo_front_test.yunlong_sales_data', values)
