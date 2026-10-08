# Modulo crm.lead
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Opción 1 (Recomendada): Usar el modelo nativo de términos de pago de Odoo
    payment_term_id = fields.Many2one(
        'account.payment.term',
        string='Condición de Pago'
    )

    # Opción 2: Mantener tu campo Selection si prefieres un texto fijo simple
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