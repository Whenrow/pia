# -*- coding: utf-8 -*-

from odoo import models, fields


class Intervenant(models.Model):
    _name = 'pia.intervenant'
    _description = 'intervenant'

    name = fields.Char(required=True)
    fase = fields.Char('FASE', required=True)
    fonction = fields.Selection([
        ('instit', 'Instituteur/trice'),
        ('logo', 'Logopède'),
        ('as-pms', 'AS-PMS'),
        ('as-pms-spe', 'AS-PMS-SPE'),
        ('psy-pms', 'PSY-PMS'),
        ('psy-pms-spe', 'PSY-PMS-SPE'),
        ('inf-pms', 'INF-PMS'),
        ('directeur', 'Directeur/trice'),
        ('logo-ext', 'LOGO-Ext'),
        ('titulaire', 'Titulaire'),
        ('coordinateur', 'Coordinateur/trice')
    ], required=True)
    telephone = fields.Char()
    email = fields.Char()
    implantation_id = fields.Many2one('pia.implantation', 'Organisme')
