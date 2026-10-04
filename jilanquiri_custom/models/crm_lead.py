from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Campos basados en los requerimientos de Jilanquiri SAC
    condicion_pago_requerida = fields.Selection([
        ('contado', 'Al Contado'),
        ('credito', 'Al Crédito')
    ], string='Condición de Pago (Requerida)', default='contado')

    tiempo_entrega_dias = fields.Integer(
        string='Tiempo de Entrega (Días útiles)', 
        default=15
    )

    requiere_certificado_calidad = fields.Boolean(
        string='Requiere Certificado (EPP/Seguridad)'
    )

    contacto_tecnico = fields.Char(
        string='Atención / Contacto Técnico'
    )