""" 
Descripción del módulo: Este módulo añade campos técnicos del proyecto a la oportunidad y a la cotización, dandonos una mejor gestión de los proyectos desde el CRM y las ventas.
Campos añadidos a la oportunidad (crm.lead): --> modulo crm_project_custom
- project_odoo_version: Versión de Odoo del proyecto (Selection)
- project_user_count: Número de usuarios del proyecto (Integer)
- project_hours: Horas estimadas del proyecto (Float)
- project_type: Tipo de proyecto (Selection)
- project_technical_id: Responsable técnico del proyecto (Many2one a res.users)
Campos añadidos a la cotización (sale.order): --> modulo crm_project_custom
- project_odoo_version: Versión de Odoo del proyecto (Selection)
- project_user_count: Número de usuarios del proyecto (Integer)
- project_hours: Horas estimadas del proyecto (Float)
- project_type: Tipo de proyecto (Selection)
- project_technical_id: Responsable técnico del proyecto (Many2one a res.users)
Lógica de transferencia:
- Cuando se selecciona una oportunidad en la cotización, los campos técnicos del proyecto se copian automáticamente desde la oportunidad a la cotización.
- Si no hay oportunidad vinculada, los campos técnicos del proyecto en la cotización se limpian.
"""




from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    project_odoo_version = fields.Selection([
        ('16', 'Odoo 16'),
        ('17', 'Odoo 17'),
        ('18', 'Odoo 18'),
        ('19', 'Odoo 19')

    ], string='Versión de Odoo')

    project_user_count = fields.Integer(string='Número de usuarios')

    project_hours = fields.Float(string='Horas estimadas del proyecto')

    project_type = fields.Selection([
        ('implementation', 'Implementación'),
        ('development', 'Desarrollo'),
        ('support', 'Soporte'),
        ('consulting', 'Consultoría')
    ], string='Tipo de proyecto')

    project_technical_id = fields.Many2one(
        'res.users', 
        string='Responsable técnico'
    )