from odoo import models, fields

class evaluacion(models.Model):
    _name='gestion_estudiantes.evaluacion'
    _description='Evaluación'

    name = fields.Char(string='Nombre de la evaluacion', required=True)
    student_id = fields.Many2one('gestion_estudiantes.estudiante', string='Estudiante', required=True)
    date = fields.Date(string='Fecha de evaluación', required=True)
    calification = fields.Float(string='Nota', required=True)
    comments = fields.Text(string='comentarios')
    subject_id = fields.Many2one('gestion_estudiantes.asignatura', string= 'Asignatura', required=True, ondelete='cascade')
    calification_ids = fields.One2many('gestion_estudiantes.calificacion', 'evaluation_id', string = 'Calificaciones asociadas')