# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Implantation(models.Model):
    _name = 'tipwit_base.implantation'
    _description = 'implantation'
    _order = 'name'

    name = fields.Char(required=True)
    active = fields.Boolean('Active', default=True)
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

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        self.env.user._compute_allowed_implantation_ids()
        return res
