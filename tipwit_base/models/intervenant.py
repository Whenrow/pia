# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Intervenant(models.Model):
    _inherit = 'res.partner'

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
        ('psycho-edu', 'Psycho-éducatrice'),
        ('psychomot', 'Psychomotricienne'),
        ('exterieur', 'Intervenant extérieur'),
        ('autre', 'Autre')
    ], required=True, default="autre")
    telephone = fields.Char()
    email = fields.Char()
    implantation_id = fields.Many2one('tipwit_base.implantation', 'Organisme')


class Users(models.Model):
    _inherit = 'res.users'

    implantation_ids = fields.Many2many('tipwit_base.implantation', string="Implantations")
    allowed_implantation_ids = fields.Many2many('tipwit_base.implantation', compute='_compute_allowed_implantation_ids')

    def _compute_allowed_implantation_ids(self):
        for user in self:
            if user.implantation_ids and not user.has_group('tipwit_base.group_tipwit_manager'):
                user.allowed_implantation_ids = user.implantation_ids
            else:
                user.allowed_implantation_ids = self.env['tipwit_base.implantation'].search([]).ids
