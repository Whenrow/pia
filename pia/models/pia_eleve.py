# -*- coding: utf-8 -*-

from odoo import models, fields


class Eleve(models.Model):
    _name = 'pia.eleve'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = 'eleve'

    name = fields.Char()
    implantation_id = fields.Many2one('pia.implantation', 'Implantation')
    date_naissance = fields.Date('Date de naissance')
    rue = fields.Char()
    ville = fields.Char()
    langue_maison = fields.Char('Langue parlée à la maison')

    # Tuteurs
    nom_tuteur_1 = fields.Char('Nom')
    statut_tuteur_1 = fields.Selection([
        ('pere', 'Père'),
        ('mere', 'Mère'),
        ('tuteur', 'Tuteur légal')
    ], 'Statut')
    telephone_tuteur_1 = fields.Char('Téléphone')
    email_tuteur_1 = fields.Char('Email')
    nom_tuteur_2 = fields.Char('Nom')
    statut_tuteur_2 = fields.Selection([
        ('pere', 'Père'),
        ('mère', 'Mère'),
        ('tuteur', 'Tuteur légal')
    ], 'Statut')
    telephone_tuteur_2 = fields.Char('Téléphone')
    email_tuteur_2 = fields.Char('Email')

    # Infos
    parcours = fields.Text('Parcours scolaire')
    objectif_integration = fields.Text('Objectifs intégration')
    bilan_medical = fields.Text('Bilan médical')
    situation_psycho_sociale = fields.Text('Situation psycho-sociale')
    diagnostic = fields.Text('Diagnostic')
    intervenants_ext = fields.Text('Intervenant Extérieurs')


class Trouble(models.Model):
    _name = 'pia.trouble'
    _decription = 'Troubles'

    name = fields.Char()
