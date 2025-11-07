from odoo import models, fields
class Calificacion(models.Model):
    _name='gestion_estudiantes.calificacion'
    _description='Calificación'

    score = fields.Float(string='Puntuación', requiered= True)
    date = fields.Char(string='Fecha de calificación', requiered= True)
    student_id = fields.Many2one('gestion_estudiantes.estudiante', string= 'Estudiante')
    evaluation_id = fields.Many2one('gestion_estudiantes.evaluacion', string='Evaluación')
    comments = fields.Text(string='Comentarios')