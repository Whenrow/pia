# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SyntheseLogo(models.Model):
    _name = 'pia.synthese.logo'
    _description = 'Synthèse logopède'

    name = fields.Char(default='Nouveau')
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('tipwit_base.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id',string='Implantation')

    # Observations
    ressources = fields.Text('Ressources')
    difficultes = fields.Text('Difficultés')
    objectifs = fields.Text('Objectifs logo de l\'année')
    outils = fields.Text('Outils mis en place')
    pistes = fields.Text('Pistes à travailler pour l\'année prochaine')

    @api.model
    def create(self, values):
        if not values.get('name'):
            values['name'] = self.env['ir.sequence'].next_by_code('pia.synthese.logo') or 'Nouveau'
        return super().create(values)
