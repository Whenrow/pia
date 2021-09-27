# -*- coding: utf-8 -*-
{
    'name': "Tipwit base",

    'summary': """Module technique Tipwit de base""",

    'description': """ Ce module défini les modèles """,
    'author': "William Henrotin",
    'website': "http://dodys.be",
    'sequence': 1,

    'category': 'Enseignement',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/tipwit_security.xml',
        'security/ir.model.access.csv',
        'views/eleve_views.xml',
        'views/intervenant_views.xml',
        'views/amenagement_views.xml',
        'views/implantation_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
