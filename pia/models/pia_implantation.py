# -*- coding: utf-8 -*-

from odoo import models, fields


class Implantation(models.Model):
    _name = 'pia.implantation'
    _description = 'implantation'

    name = fields.Char(required=True)
    fase = fields.Char('FASE', required=True)
    reseau = fields.Selection([
        ('libre', 'Libre'),
        ('communal', 'Communal'),
        ('federation', 'Fédération Wallonie-Bruxelles'),
        ('autre', 'Autre')
    ], required=True)
    direction = fields.Char()
    telephone = fields.Char()
    gsm = fields.Char()
    email = fields.Char()
