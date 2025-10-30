from odoo import models, fields

class Asignatura(models.Model):
    _name='gestion_estudiantes.asignatura'
    _description='Asignatura'

    name = fields.Char(string ='Nombre de la asignatura', required=True)
    code = fields.Char(string ='Código de la asignatura', required=True)
    student_ids = fields.Many2many('gestion_estudiantes.estudiante', relation='asignatura_estudiante_rel', string='Estudiantes inscritos en la asignatura')