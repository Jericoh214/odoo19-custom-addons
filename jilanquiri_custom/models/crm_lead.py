# -*- coding: utf-8 -*-
from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_plazo_entrega = fields.Char(
        string='Plazo de Entrega',
        help='Tiempo o plazo de entrega acordado con el cliente (ej. 3 a 5 días útiles)'
    )
    x_disponibilidad_stock = fields.Char(
        string='Disponibilidad',
        help='Disponibilidad estimada (ej. Stock Inmediato / A pedido)'
    )
    x_marca_sugerida = fields.Char(
        string='Marca Sugerida',
        help='Marca principal sugerida o requerida por el cliente'
    )

    def _prepare_opportunity_quotation_context(self):
        """
        Extiende el contexto para que al crear un presupuesto desde la oportunidad,
        los datos comerciales viajen automáticamente a la cotización (sale.order).
        """
        quotation_context = super()._prepare_opportunity_quotation_context()
        quotation_context.update({
            'default_x_plazo_entrega': self.x_plazo_entrega,
            'default_x_disponibilidad_stock': self.x_disponibilidad_stock,
            'default_x_marca_sugerida': self.x_marca_sugerida,
        })
        return quotation_context
