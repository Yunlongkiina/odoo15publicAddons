# -*- coding: utf-8 -*-
# from odoo import http


# class OdooLearningHospitalManagement(http.Controller):
#     @http.route('/odoo_learning_hospital_management/odoo_learning_hospital_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

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
