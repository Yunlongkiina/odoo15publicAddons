# -*- coding: utf-8 -*-
# from odoo import http
# import json


# class OdooLearningHospitalManagement(http.Controller):
#     @http.route('/react', cors='*', auth='public')
#     def index(self, **kw):
#         all_products = http.request.env['product.product'].sudo().search([])
#         product_name = []
#         for item in all_products:
#             product_name.append(item.name)
#         return json.dumps({'data': product_name})

#     @http.route('/react/products', auth='public')
#     def showproduct(self, **kw):
#         return {
#             'success': True,
#             'status': 'OK',
#             'code': 200
#         }

#     @http.route('/odoo_learning_hospital_management/odoo_learning_hospital_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_learning_hospital_management.listing', {
#             'root': '/odoo_learning_hospital_management/odoo_learning_hospital_management',
#             'objects': http.request.env['odoo_learning_hospital_management.odoo_learning_hospital_management'].search([]),
#         })

#     @http.route('/odoo_learning_hospital_management/odoo_learning_hospital_management/objects/<model("odoo_learning_hospital_management.odoo_learning_hospital_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_learning_hospital_management.object', {
#             'object': obj
#         })
