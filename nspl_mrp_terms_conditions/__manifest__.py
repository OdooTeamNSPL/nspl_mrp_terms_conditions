{
    'name': 'MRP Terms & Conditions',
    'version': '17.0',
    'summary': 'Configure Terms & Conditions for Manufacturing Orders',
    'description': """
    Configure and print Terms & Conditions in Manufacturing Orders.

    ✔ Define standard terms for manufacturing  
    ✔ Automatically load conditions into MO 

    Helps ensure compliance and consistency across production workflows.
    """,
    'category': 'Manufacturing',
    'sequence': 4,
    'author': 'Namah Softech Private Limited',
    'website': 'http://www.namahsoftech.com',
    'license': 'LGPL-3',
    'support': 'support@namahsoftech.com',
    'price': 9.99,
    'currency': 'USD',
    'contributors': ['Shivani Solanki'],
    'depends': ['mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_terms_views.xml',
        'views/mrp_production_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
