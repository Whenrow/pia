# -*- coding: utf-8 -*-

from odoo import models, fields


class Eleve(models.Model):
    _inherit = 'pia.eleve'

    suivi_1 = fields.Many2one('pia.intervenant','Suivi PARI 1')
    suivi_2 = fields.Many2one('pia.intervenant','Suivi PARI 2')

    #Partenariats
    logo = fields.Many2one('pia.intervenant','Logopède')
    ergo = fields.Many2one('pia.intervenant','Ergothérapeute')
    kine = fields.Many2one('pia.intervenant','Kinésithérapeute')
    psy = fields.Many2one('pia.intervenant','Psy')
    neuropsy = fields.Many2one('pia.intervenant','Neuropsy')
    pedopsy = fields.Many2one('pia.intervenant','Pédopsy')
    orthoptiste = fields.Many2one('pia.intervenant','Orthoptiste')
    neuroped = fields.Many2one('pia.intervenant','Neuropédiatre')
    orthopeda = fields.Many2one('pia.intervenant','Orthopédagoque')
    kinesio = fields.Many2one('pia.intervenant','Kinésiologue')
    osteo = fields.Many2one('pia.intervenant','Ostéopathe')
    autre = fields.Text('Autre')

    protocole_ids = fields.One2many('pari.protocole.ar', 'eleve_id')
    dac_ids = fields.One2many('pari.dac', 'eleve_id')

    adresse_tuteur_1 = fields.Char('Adresse')
    adresse_tuteur_2 = fields.Char('Adresse')

    def action_view_table(self):
        self.ensure_one()
        action = self.env.ref('pari.action_view_table').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

    def action_view_observation(self):
        self.ensure_one()
        action = self.env.ref('pari.action_view_observation').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

    def action_view_protocole(self):
        self.ensure_one()
        action = self.env.ref('pari.action_view_protocole').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

    def action_view_dac(self):
        self.ensure_one()
        action = self.env.ref('pari.action_view_dac').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

    def action_view_entretien(self):
        self.ensure_one()
        action = self.env.ref('pia.action_view_entretien').read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

