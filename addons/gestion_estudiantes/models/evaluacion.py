from odoo import models, fields

class evaluacion(models.Model):
    _name='gestion_estudiantes.evaluacion'
    _description='Evaluación'

    student_id = fields.Many2one('gestion_estudiantes.estudiante', string='Estudiante', required=True)
    date = fields.Date(string='Fecha de evaluación', required=True)
    calification = fields.Float(string='Nota', required=True)
    comments = fields.Text(string='comentarios')
