# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
    ])
    direction = fields.Char()
    telephone = fields.Char()
    gsm = fields.Char()
    email = fields.Char()

    @api.model
    def create(self, vals):
        res = super().create(vals)
        # Hacky tricks to recompute the allowed implantation ASAP in case it is use right after
        self.env.user._compute_allowed_implantation_ids()
        return res
