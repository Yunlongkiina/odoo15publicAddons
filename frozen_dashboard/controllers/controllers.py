# -*- coding: utf-8 -*-
# from odoo import http


# class FrozenDashboard(http.Controller):
#     @http.route('/frozen_dashboard/frozen_dashboard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/frozen_dashboard/frozen_dashboard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('frozen_dashboard.listing', {
#             'root': '/frozen_dashboard/frozen_dashboard',
#             'objects': http.request.env['frozen_dashboard.frozen_dashboard'].search([]),
#         })

#     @http.route('/frozen_dashboard/frozen_dashboard/objects/<model("frozen_dashboard.frozen_dashboard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('frozen_dashboard.object', {
#             'object': obj
#         })
