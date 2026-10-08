from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Campos que viajan automáticamente desde el CRM
    condicion_pago_requerida = fields.Selection(
        related='opportunity_id.condicion_pago_requerida',
        string='Condición de Pago (CRM)',
        readonly=False
    )
    
    tiempo_entrega_dias = fields.Integer(
        related='opportunity_id.tiempo_entrega_dias',
        string='Tiempo de Entrega (Días útiles)',
        readonly=False
    )
    
    requiere_certificado_calidad = fields.Boolean(
        related='opportunity_id.requiere_certificado_calidad',
        string='Requiere Certificado',
        readonly=False
    )
    
    contacto_tecnico = fields.Char(
        related='opportunity_id.contacto_tecnico',
        string='Contacto Técnico',
        readonly=False
    )