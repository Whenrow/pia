# -*- coding: utf-8 -*-

from odoo import models, fields


class Eleve(models.Model):
    _name = 'tipwit_base.eleve'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = 'eleve'
    _order = 'annee_etude, name'

    name = fields.Char()
    active = fields.Boolean('Active', default=True)
    implantation_id = fields.Many2one('tipwit_base.implantation', 'Implantation')
    date_naissance = fields.Date('Date de naissance')
    rue = fields.Char()
    ville = fields.Char()
    langue_maison = fields.Char('Langue parlée à la maison')

    # Tuteurs
    nom_tuteur_1 = fields.Char()
    statut_tuteur_1 = fields.Selection([
        ('pere', 'Père'),
        ('mere', 'Mère'),
        ('tuteur', 'Tuteur légal')
    ],)
    telephone_tuteur_1 = fields.Char()
    email_tuteur_1 = fields.Char()
    nom_tuteur_2 = fields.Char()
    statut_tuteur_2 = fields.Selection([
        ('pere', 'Père'),
        ('mère', 'Mère'),
        ('tuteur', 'Tuteur légal')
    ])
    telephone_tuteur_2 = fields.Char()
    email_tuteur_2 = fields.Char()

    # Infos
    parcours = fields.Text('Parcours scolaire')
    objectif_integration = fields.Text('Objectifs intégration')
    bilan_medical = fields.Text('Bilan médical')
    situation_psycho_sociale = fields.Text('Situation psycho-sociale')
    diagnostic = fields.Text('Diagnostic')
    intervenants_ext = fields.Text('Intervenant Extérieurs')
    annee_etude = fields.Selection([
       ('m1', 'M1'),
       ('m2', 'M2'),
       ('m3', 'M3'),
       ('p1', 'P1'),
       ('p1b', 'P1 bis'),
       ('p2', 'P2'),
       ('p2b', 'P2 bis'),
       ('p3', 'P3'),
       ('p3b', 'P3 bis'),
       ('p4', 'P4'),
       ('p4b', 'P4 bis'),
       ('p5', 'P5'),
       ('p5b', 'P5 bis'),
       ('p6', 'P6'),
       ('p6b', 'P6 bis'),
       ('s1', 'S1'),
       ('s2', 'S2'),
       ('s3', 'S3'),
       ('s4', 'S4'),
       ('s5', 'S5'),
       ('s6', 'S6')
    ], string='Année d\'étude')
    insti_id = fields.Many2one('res.partner','Instit intégration')
    logo_id = fields.Many2one('res.partner','Logo intégration')
    coordi_id = fields.Many2one('res.partner','Coordinateur intégration')

    suivi = fields.Selection([
        ('none', 'Aucun'),
    ], 'Type de suivi')
