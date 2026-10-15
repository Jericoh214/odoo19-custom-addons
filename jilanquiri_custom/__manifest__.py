{
    'name': 'Jilanquiri Custom',
    'version': '1.0',
    'summary': 'Adaptación de CRM y Ventas para Jilanquiri SAC',
    'author': 'Jerico',
    'category': 'Sales/CRM',
    'depends': ['crm', 'sale_management'],
    'data': [
        'views/crm_lead_views.xml',
        'views/sale_order_views.xml',
        'views/report_saleorder_custom.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}