{
    'name': 'Delivery Product Description',
    'version': '18.0.1.0.0',
    'summary': 'Show product description in Delivery Orders & PDF',
    'depends': ['stock', 'sale_stock'],
    'data': [
  #      'views/stock_picking_view.xml',
        'reports/report_deliveryslip.xml',
    ],
    'installable': True,
    'application': False,
}
