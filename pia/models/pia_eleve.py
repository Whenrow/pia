# -*- coding: utf-8 -*-

from odoo import models, fields


class Eleve(models.Model):
    _inherit = 'tipwit_base.eleve'

    conseil_count = fields.Integer(compute='_compute_conseil_count')
    reunion_count = fields.Integer(compute='_compute_conseil_count')
    synthese_count = fields.Integer(compute='_compute_conseil_count')
    bilan_count = fields.Integer(compute='_compute_conseil_count')
    entretien_count = fields.Integer(compute='_compute_conseil_count')

    suivi = fields.Selection(selection_add=[
        ('integ', 'Intégration'),
    ])

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
    _description = 'Troubles'

    name = fields.Char()
