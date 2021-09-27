# -*- coding: utf-8 -*-
{
    'name': "PARI",

    'summary': """
        Gestion des élèves de l'enseignement primaire suivis dans le cadre du PARI. """,

    'description': """
        Ce module permet aux écoles de garder trace de leur conseil de classe par
        élèves. Des rapport internes et externes sont disponibles pour les parents
        ainsi que les archive internes de l'école
        """,
    'author': "William Henrotin",
    'website': "http://dodys.be",
    'sequence': 2,

    'category': 'Enseignement',
    'version': '1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['tipwit_base'],

    # always loaded
    'data': [
        'security/pari_security.xml',
        'security/ir.model.access.csv',
        'reports/pari_reports.xml',
        'reports/report_protocole.xml',
        'views/pia_eleve_views.xml',
        'views/pari_document_views.xml',
        'views/menus.xml',
    ],
    'license': 'LGPL-3',
}
