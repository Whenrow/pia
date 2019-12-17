# -*- coding: utf-8 -*-

from odoo import models, fields


class Objectif(models.Model):
    _name = 'pia.objectif'
    _description = 'Objectifs'

    objectif = fields.Text(required=True)
    outil = fields.Char('Outils')
    commentaire = fields.Char('Commentaires')
    moyen = fields.Char('Moyen')
    conseil_id = fields.Many2one('pia.conseil')
    evaluation = fields.Selection([
        ('atteint', 'Atteint'),
        ('non_atteint', 'Non atteint'),
        ('abandonne', 'Abandonné')
    ])
