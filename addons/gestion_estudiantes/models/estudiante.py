from odoo import models, fields
class Estudiante(models.Model):
    _name='gestion_estudiantes.estudiante'
    _description='Estudiante'

    name = fields.char(string='Nombre', required=True)
    age = fields.integer(string='Edad')
    email = fields.char(string='Correo Electrónico')
    photo = fields.binary(string='Foto')
    enrollment_date = fields.date(string='Fecha de Inscripción')
    active = fields.boolean(string='Activo', default=True)
    grade = fields.selection([
        ('primero', 'Primero'),
        ('segundo', 'Segundo'),
        ('tercero', 'Tercero'),
        ('cuarto', 'Cuarto'),
        ('quinto', 'Quinto')
    ], string='Grado')
    address = fields.char(string='Dirección')
    phone = fields.char(string='Teléfono')

