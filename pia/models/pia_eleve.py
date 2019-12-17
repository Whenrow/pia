# -*- coding: utf-8 -*-

from odoo import models, fields


class Eleve(models.Model):
    _name = 'pia.eleve'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'eleve'

    name = fields.Char()
    implantation_id = fields.Many2one('pia.implantation', 'Implantation')
    date_naissance = fields.Date('Date de naissance')
    rue = fields.Char()
    ville = fields.Char()
    langue_maison = fields.Many2one('res.lang', 'Langue parlée à la maison')

    # Tuteurs
    nom_tuteur_1 = fields.Char('Nom')
    statut_tuteur_1 = fields.Selection([
        ('pere', 'Père'),
        ('mère', 'Mère'),
        ('tuteur', 'Tuteur légal')
    ], 'Status')
    telephone_tuteur_1 = fields.Char('Téléphone')
    email_tuteur_1 = fields.Char('Email')
    nom_tuteur_2 = fields.Char('Nom')
    statut_tuteur_2 = fields.Selection([
        ('pere', 'Père'),
        ('mère', 'Mère'),
        ('tuteur', 'Tuteur légal')
    ], 'Status')
    telephone_tuteur_2 = fields.Char('Téléphone')
    email_tuteur_2 = fields.Char('Email')

    # Infos
    parcours = fields.Text('Parcours scolaire')
    objectif_integration = fields.Char('Objectifs intégration')
    bilan_medical = fields.Char('Bilan médical')
    situation_psycho_sociale = fields.Char('Situation psycho-sociale')
    diagnostique = fields.Char('Diagnostique')


class Trouble(models.Model):
    _name = 'pia.trouble'
    _decription = 'Troubles'

    name = fields.Char()
