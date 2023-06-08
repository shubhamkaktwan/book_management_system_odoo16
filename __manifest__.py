{
    'name':'Books Management System by Shubham Kaktwan ',
        'summary': """
        this is the library management module made using odoo16""",

    'description': """
        This description contains the info about this module in brief.
    """,

    'author': "Shubham",
    'website': "https://www.odoo.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],
    'sequence': -5,

    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/book_books.xml',
        'views/book_history_view.xml',
        'views/book_id_sequence_gen.xml',
    ],

}