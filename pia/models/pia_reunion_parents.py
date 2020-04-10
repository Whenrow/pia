# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReunionParents(models.Model):
    _name = 'pia.reunion.parents'
    _description = 'Rèunion de parents'

    name = fields.Char(default='Nouveau')
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('pia.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id',string='Implantation')
    intervenant_ids = fields.Many2many(
        'pia.intervenant',
        'pia_intervant_pia_reunion_rel',
        'intervenant_id',
        'reunion_id'
    )

    # Observations
    resume_parents = fields.Text('Résumé parents')
    resume_integration = fields.Text('Résumé intégration')
    resume_ecole = fields.Text('Résumé école ordinaire')
    resume_pms = fields.Text('Résumé PMS')

    @api.onchange('eleve_id')
    def _onchange_eleve_id(self):
        self.intervenant_ids = [(5, 0, 0)]
        if self.eleve_id:
            reunion = self.env['pia.reunion.parents'].search([
                ('eleve_id', '=', self.eleve_id.id),
            ])
            if reunion - self:
                self.intervenant_ids = [(6, 0, (reunion - self)[0].intervenant_ids.ids)]
