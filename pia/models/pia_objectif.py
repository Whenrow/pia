# -*- coding: utf-8 -*-

from odoo import models, fields


class Objectif(models.Model):
    _name = 'pia.objectif'
    _description = 'Objectifs'

    objectif = fields.Text()
    outil = fields.Text('Outils')
    commentaire = fields.Text('Commentaires')
    moyen = fields.Text('Moyen')
    conseil_id = fields.Many2one('pia.conseil', invisible=True)
    evaluation = fields.Selection([
        ('atteint', 'Atteint'),
        ('non_atteint', 'Non atteint'),
        ('abandonne', 'Abandonné')
    ])
    is_instit = fields.Boolean('Instit')
    is_logo = fields.Boolean('Logo')
    is_titulaire = fields.Boolean('Titulaire')
