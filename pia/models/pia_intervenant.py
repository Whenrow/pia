# -*- coding: utf-8 -*-

from odoo import models, fields


class Intervenant(models.Model):
    _name = 'pia.intervenant'
    _description = 'intervenant'
    _order = 'name'

    name = fields.Char(required=True, string='Noms')
    fonction = fields.Selection([
        ('instit', 'Instituteur/trice intégration'),
        ('logo', 'Logopède intégration'),
        ('as-pms', 'AS-PMS ordinaire'),
        ('as-pms-spe', 'AS-PMS spécialisé'),
        ('psy-pms', 'PSY-PMS ordinaire'),
        ('psy-pms-spe', 'PSY-PMS spécialisé'),
        ('inf-pms', 'INF-PMS ordinaire'),
        ('inf-pms-spe', 'INF-PMS spécialisé'),
        ('directeur', 'Directeur/trice ordinaire'),
        ('directeur_int', 'Directrice intégration'),
        ('logo-ext', 'logopède extérieur'),
        ('titulaire', 'Titulaire ordinaire'),
        ('coordinateur', 'Coordinateur/trice intégration'),
        ('neuropsy-int', 'Neuropsy intégration'),
        ('exterieur', 'Intervenant extérieur'),
        ('autre', 'Autre')
    ], required=True)
    telephone = fields.Char()
    email = fields.Char()
    implantation_id = fields.Many2one('pia.implantation', 'Organisme')
    user_id = fields.Many2one('res.users', 'Utilisateur')
    allowed_implantation_ids = fields.Many2many(
        'pia.implantation',
        'pia_implantation_pia_intervenant_rel',
        'intervenant_id',
        'conseil_id',
        'Implantations autorisées'
    )


class Users(models.Model):
    _inherit = 'res.users'

    intervenant_ids = fields.One2many('pia.intervenant', 'user_id')
    allowed_implantation_ids = fields.One2many('pia.implantation', compute="_compute_allowed_implantation_ids")

    def _compute_allowed_implantation_ids(self):
        for user in self:
            if user.intervenant_ids.allowed_implantation_ids:
                user.allowed_implantation_ids = user.intervenant_ids.allowed_implantation_ids
            else:
                user.allowed_implantation_ids = self.env['pia.implantation'].search([]).ids
