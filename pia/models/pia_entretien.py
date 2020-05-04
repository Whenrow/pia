# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EntretienExterieur(models.Model):
    _name = 'pia.entretien'
    _description = 'Entretiens Extérieurs'

    name = fields.Char(default='Nouveau')
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('pia.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id',string='Implantation')

    # Observations
    intervenants = fields.Text('Intervenant')
    entretien = fields.Text('Entretien')
