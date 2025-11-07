from odoo import models, fields

class Asignatura(models.Model):
    _name='gestion_estudiantes.asignatura'
    _description='Asignatura'
    def _get_default_teacher(self):
        teacher= self.env['res.partner'].search([('is_teacher', '=', True), ('email', '=', 'profe_principal@gmail.com')], limit=1).id
        return teacher

    name = fields.Char(string ='Nombre de la asignatura', required=True)
    code = fields.Char(string ='Código de la asignatura', required=True)
    course_start = fields.Char(string='Fecha de inicio', default=fields.Date.today())
    course_end = fields.Char(string='Fecha de finalización')
    student_ids = fields.Many2many('gestion_estudiantes.estudiante', relation='asignatura_estudiante_rel', string='Estudiantes inscritos en la asignatura')
    evaluations_ids = fields.One2many('gestion_estudiantes.evaluacion', 'subject_id', string='Evaluaciones de la asignatura')
    teacher_id = fields.Many2one('res.partner', string='Profesor', domain=[('is_teacher', '=', True)], default=_get_default_teacher, ondelete='cascade')
    teacher_email = fields.Char(related='teacher_id.email')
    state = fields.Selection([('por_registrar', 'Por registrar'), ('en_curso', 'En curso'), ('finalizada', 'Finalizada')], string='Estado', default='por_registrar')