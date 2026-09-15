from odoo import models, fields, api
#se importa api para poder usar el decorador @api.onchange
class SaleOrder(models.Model):
    _inherit = 'sale.order' #inherit de sale.order para añadir campos técnicos del proyecto a la cotización

    project_odoo_version = fields.Selection([ #versiones de Odoo disponibles para el proyecto
        ('16', 'Odoo 16'),
        ('17', 'Odoo 17'),
        ('18', 'Odoo 18'),
        ('19', 'Odoo 19')
    ], string='Versión de Odoo')

    project_user_count = fields.Integer(string='Número de usuarios') # Número de usuarios del proyecto

    project_hours = fields.Float(string='Horas estimadas del proyecto') # Horas estimadas del proyecto

# Tipo de proyecto
    project_type = fields.Selection([
        ('implementation', 'Implementación'),
        ('development', 'Desarrollo'),
        ('support', 'Soporte'),
        ('consulting', 'Consultoría')
    ], string='Tipo de proyecto') 

    project_technical_id = fields.Many2one( #Relacion many2one para seleccionar el responsable técnico del proyecto
        'res.users', 
        string='Responsable técnico'
    )
    
    # --- LÓGICA DE TRANSFERENCIA ---
    @api.onchange('opportunity_id') # decorador para ejecutar la función cuando se cambie el campo opportunity_id
    def _onchange_opportunity_id_project_data(self):
        # Si la cotización tiene una oportunidad vinculada, copiamos los datos
        if self.opportunity_id:
            self.project_odoo_version = self.opportunity_id.project_odoo_version
            self.project_user_count = self.opportunity_id.project_user_count
            self.project_hours = self.opportunity_id.project_hours
            self.project_type = self.opportunity_id.project_type
            self.project_technical_id = self.opportunity_id.project_technical_id
#        Sirven para transferir los datos del proyecto de la oportunidad a la cotización,  
#        pasa de la oportunidad a la cotización los campos técnicos del proyecto.
#        Si no hay oportunidad vinculada, se limpian los campos