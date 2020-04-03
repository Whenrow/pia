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
    conseil_count = fields.Integer(compute='_compute_conseil_count')
    reunion_count = fields.Integer(compute='_compute_conseil_count')
    synthese_count = fields.Integer(compute='_compute_conseil_count')

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

    def _compute_conseil_count(self):
        for eleve in self:
            synthese_count = self.env['pia.synthese.logo'].search_count([
                ('eleve_id', '=', eleve.id)
            ])
            reunion_count = self.env['pia.reunion.parents'].search_count([
                ('eleve_id', '=', eleve.id)
            ])
            conseil_count = self.env['pia.conseil'].search_count([
                ('eleve_id', '=', eleve.id)
            ])
            eleve.conseil_count = conseil_count
            eleve.reunion_count = reunion_count
            eleve.synthese_count = synthese_count

    def action_view_synthese(self):
        self.ensure_one()
        action = self.env.ref('pia.action_view_synthese').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

    def action_view_reunion(self):
        self.ensure_one()
        action = self.env.ref('pia.action_view_reunion').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

    def action_view_conseil(self):
        self.ensure_one()
        action = self.env.ref('pia.action_view_conseil').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action


class Trouble(models.Model):
    _name = 'pia.trouble'
    _decription = 'Troubles'

    name = fields.Char()
