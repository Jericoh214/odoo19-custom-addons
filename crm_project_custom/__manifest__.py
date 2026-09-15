"""
Este archivo es el manifiesto del módulo crm_project_custom, que añade campos técnicos del proyecto a la oportunidad y a la cotización en Odoo.
El manifiesto define la información básica del módulo, como su nombre, versión, autor, categoría, dependencias y archivos de datos.
Además, se especifica que el módulo es instalable y no es una aplicación independiente, y se indica la licencia bajo la cual se distribuye.
"""

{
    'name': 'Personalización de CRM a Ventas',
    'version': '1.0',
    'summary': 'Añade campos técnicos en CRM',
    'author': 'Jerico',
    'category': 'Sales/CRM',
    'depends': ['crm', 'sale_management'],
    'data': [
        'views/crm_lead_views.xml',
        'views/sale_order_views.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}