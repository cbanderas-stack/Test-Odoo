from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='Es profesor', default=False)
    speciality = fields.Char(string='Especialidad')
    date_started = fields.Date(string='Fecha de inicio')
    salary = fields.Float(string='Salario')

