# -*- coding: utf-8 -*-

from odoo import models, fields


class Eleve(models.Model):
    _name = 'pia.eleve'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = 'eleve'
    _order = 'annee_etude, name'

    name = fields.Char()
    active = fields.Boolean('Active', default=True)
    implantation_id = fields.Many2one('pia.implantation', 'Implantation')
    date_naissance = fields.Date('Date de naissance')
    rue = fields.Char()
    ville = fields.Char()
    langue_maison = fields.Char('Langue parlée à la maison')
    conseil_count = fields.Integer(compute='_compute_conseil_count')
    reunion_count = fields.Integer(compute='_compute_conseil_count')
    synthese_count = fields.Integer(compute='_compute_conseil_count')
    bilan_count = fields.Integer(compute='_compute_conseil_count')
    entretien_count = fields.Integer(compute='_compute_conseil_count')

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
    annee_etude = fields.Selection([
       ('acc', 'Accueil'),
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
       ('p6b', 'P6 bis')
    ], string='Année d\'étude')
    insti_id = fields.Many2one('pia.intervenant','Instit intégration')
    logo_id = fields.Many2one('pia.intervenant','Logo intégration')
    coordi_id = fields.Many2one('pia.intervenant','Coordinateur intégration')

    suivi = fields.Selection([
        ('integ', 'Intégration'),
        ('pari', 'PARI')
    ], 'Type de suivi')

    def _compute_conseil_count(self):
        for eleve in self:
            synthese_count = self.env['pia.synthese.logo'].sudo().sudo().search_count([
                ('eleve_id', '=', eleve.id)
            ])
            reunion_count = self.env['pia.reunion.parents'].sudo().search_count([
                ('eleve_id', '=', eleve.id)
            ])
            conseil_count = self.env['pia.conseil'].sudo().search_count([
                ('eleve_id', '=', eleve.id)
            ])
            bilan_count = self.env['pia.bilan.logo'].sudo().search_count([
                ('eleve_id', '=', eleve.id)
            ])
            entretien_count = self.env['pia.entretien'].sudo().search_count([
                ('eleve_id', '=', eleve.id)
            ])
            eleve.conseil_count = conseil_count
            eleve.reunion_count = reunion_count
            eleve.synthese_count = synthese_count
            eleve.bilan_count = bilan_count
            eleve.entretien_count = entretien_count

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

    def action_view_entretien(self):
        self.ensure_one()
        action = self.env.ref('pia.action_view_entretien').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

    def action_view_bilan(self):
        self.ensure_one()
        action = self.env.ref('pia.action_view_bilan').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

class Trouble(models.Model):
    _name = 'pia.trouble'
    _decription = 'Troubles'

    name = fields.Char()
