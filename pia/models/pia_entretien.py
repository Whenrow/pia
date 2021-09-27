# -*- coding: utf-8 -*-

from odoo import models, fields


class EntretienExterieur(models.Model):
    _name = 'pia.entretien'
    _description = 'Informations complémentaires'
    _order = 'date desc'

    name = fields.Char(default='Nouveau')
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('tipwit_base.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id',string='Implantation')

    # Observations
    intervenants = fields.Text('Intervenant')
    entretien = fields.Text('Entretien')
