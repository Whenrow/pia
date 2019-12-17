# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields


class Conseil(models.Model):
    _name = 'pia.conseil'
    _description = 'Conseil de classe'

    name = fields.Selection([
        ('premier', 'Premier conseil de classe'),
        ('deuxieme', 'Deuxième conseil de classe'),
        ('troisieme', 'Troisième conseil de classe')
    ], required=True)
    date = fields.Date('Date', default=datetime.date.today)
    eleve_id = fields.Many2one('pia.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id', string='Implantation')
    responsable = fields.Many2one('pia.intervenant', 'Responsable')
    intervenant_ids = fields.Many2many(
        'pia.intervenant',
        'pia_intervant_pia_conseil_rel',
        'intervenant_id',
        'conseil_id'
    )
    trouble_ids = fields.Many2many('pia.trouble', 'pia_trouble_pia_conseil_rel', 'trouble_id', 'conseil_id')

    # Observations
    ressource = fields.Text('Ressources')
    besoin = fields.Text('Besoins')
    autre = fields.Text('Autres')

    a_faire = fields.Text('A faire')
