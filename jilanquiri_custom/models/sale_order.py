# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Condiciones comerciales heredadas / comunicadas desde CRM
    x_plazo_entrega = fields.Char(
        string='Plazo de Entrega',
        help='Plazo de entrega acordado con el cliente'
    )
    x_disponibilidad_stock = fields.Char(
        string='Disponibilidad',
        help='Disponibilidad de stock'
    )
    x_marca_sugerida = fields.Char(
        string='Marca Sugerida',
        help='Marca sugerida desde la oportunidad'
    )

    # Cuentas bancarias personalizadas de Jilanquiri SAC
    x_nro_cuenta_cte = fields.Char(
        string='Nro. Cuenta Corriente',
        default='.001108490100005995-',
        help='Cuenta Corriente del Banco BBVA'
    )
    x_nro_cci = fields.Char(
        string='Nro. CCI',
        default='.01184900010000599574-',
        help='Código de Cuenta Interbancario BBVA'
    )


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_marca = fields.Char(
        string='Marca',
        default='NACIONAL',
        help='Marca del producto para el reporte de cotización'
    )
