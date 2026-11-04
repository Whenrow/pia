# -*- coding: utf-8 -*-

from odoo import models, fields


class BilanLogo(models.Model):
    _inherit = 'pia.bilan.logo'

    bilan_type = fields.Selection(selection_add=[
        ('oral_ecrit', 'Bilan en langage oral et langage écrit'),
        ('oral_math', 'Bilan en langage oral et mathématiques'),
        ('ecrit_math', 'Bilan en langage écrit et mathématiques'),
    ])
