# -*- coding: utf-8 -*-
# from odoo import http


# class ScrubzReport(http.Controller):
#     @http.route('/scrubz_report/scrubz_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scrubz_report/scrubz_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('scrubz_report.listing', {
#             'root': '/scrubz_report/scrubz_report',
#             'objects': http.request.env['scrubz_report.scrubz_report'].search([]),
#         })

#     @http.route('/scrubz_report/scrubz_report/objects/<model("scrubz_report.scrubz_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scrubz_report.object', {
#             'object': obj
#         })

