# -*- coding: utf-8 -*-
{
    'name': "PIA",

    'summary': """
        Gerer les conseils de classe. """,

    'description': """
        Ce module permet aux écoles de garder trace de leur conseil de classe par
        élèves. Des rapport internes et externes sont disponibles pour les parents
        ainsi que les archive internes de l'école
        """,
    'author': "William Henrotin",
    'website': "http://eps-saintberthuin.be",
    'sequence': 1,

    'category': 'Enseignement',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/pia_security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'reports/pia_reports.xml',
        'reports/report_pia.xml',
        'reports/report_pv.xml',
        'reports/report_reunion_parents.xml',
        'reports/report_synthese_logo.xml',
        'reports/report_entretien.xml',
        'reports/report_bilan.xml',
        'views/pia_eleve_views.xml',
        'views/pia_intervenant_views.xml',
        'views/pia_implantation_views.xml',
        'views/pia_conseil_views.xml',
        'views/pia_reunion_parents_views.xml',
        'views/pia_amenagement_views.xml',
        'views/pia_objectif_views.xml',
        'views/pia_synthese_logo_views.xml',
        'views/pia_entretien_views.xml',
        'views/pia_bilan_logo_views.xml',
    ],
}
