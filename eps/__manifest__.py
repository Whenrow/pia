# -*- coding: utf-8 -*-
{
    'name': "EPS",

    'summary': """Specification pour EPS""",

    'description': """ """,
    'author': "William Henrotin",
    'website': "http://dodys.be",
    'sequence': 1,
    'application': True,
    'installable': True,

    'category': 'Enseignement',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['pia'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/eps_reports.xml',
        'reports/report_pia.xml',
        'reports/report_conseil.xml',
        'views/pia_eleve_views.xml',
        'views/pia_conseil_views.xml'
    ],
    'license': 'LGPL-3',
}
