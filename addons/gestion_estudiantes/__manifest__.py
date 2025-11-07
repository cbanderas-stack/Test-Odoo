{
    'name': 'Gestión de Estudiantes',
    'version': '1.0.0', ##Version Odoo 17.0
    'summary': 'Módulo para gestionar estudiantes en Odoo',
    'author': 'Cris',
    'category': 'Education',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'Views/asignatura_views.xml',
        'views/estudiante_views.xml',
        'views/evaluacion_views.xml',
        'views/profesor_views.xml',
        'views/acciones.xml',
        'views/calificaciones.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}