from odoo import models, fields
class Estudiante(models.Model):
    _name='gestion_estudiantes.estudiante'
    _description='Estudiante'

    name = fields.Char(string='Nombre', required=True)
    age = fields.Integer(string='Edad')
    email = fields.Char(string='Correo Electrónico')
    photo = fields.Binary(string='Foto')
    enrollment_date = fields.Date(string='Fecha de Inscripción')
    active = fields.Boolean(string='Activo', default=True)
    grade = fields.Selection([
        ('primero', 'Primero'),
        ('segundo', 'Segundo'),
        ('tercero', 'Tercero'),
        ('cuarto', 'Cuarto'),
        ('quinto', 'Quinto')
    ], string='Grado')
    address = fields.Char(string='Dirección')
    phone = fields.Char(string='Teléfono')
    teacher_id = fields.Many2one('res.partner', string='Profesor', domain=[('is_teacher', '=', True)])
    subject_ids = fields.Many2many('gestion_estudiantes.asignatura', relation='asignatura_estudiante_rel', string='Asignaturas')
    evaluation_ids = fields.One2many('gestion_estudiantes.evaluacion', 'student_id', string='Evaluaciones')

