# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Conseil(models.Model):
    _name = 'pia.conseil'
    _description = 'Conseil de classe'

    name = fields.Selection([
        ('premier', 'Premier conseil de classe'),
        ('deuxieme', 'Deuxième conseil de classe'),
        ('troisieme', 'Troisième conseil de classe')
    ], required=True)
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('pia.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id', string='Implantation')
    responsable_id = fields.Many2one('pia.intervenant', 'Responsable')
    intervenant_ids = fields.Many2many(
        'pia.intervenant',
        'pia_intervant_pia_conseil_rel',
        'intervenant_id',
        'conseil_id'
    )
    trouble_ids = fields.Many2many('pia.trouble', 'pia_trouble_pia_conseil_rel', 'trouble_id', 'conseil_id')
    objectifs_ids = fields.One2many('pia.objectif', 'conseil_id')
    amenagement_ids = fields.Many2many('pia.amenagement', 'pia_amenagement_pia_conseil_res', 'amenagement_id', 'conseil_id')
    allowed_amenagement_ids = fields.One2many('pia.amenagement', compute='_compute_allowed_amenagement_ids')
    report_name = fields.Char(compute='_compute_report_name')
    logo_id = fields.Many2one('pia.intervenant', compute='_compute_referals')
    instit_id = fields.Many2one('pia.intervenant', compute='_compute_referals')

    # Observations
    ressource = fields.Text('Ressources')
    besoin = fields.Text('Besoins')
    autre = fields.Text('Autres')

    a_faire = fields.Text('A faire')

    @api.depends('trouble_ids')
    def _compute_allowed_amenagement_ids(self):
        for conseil in self:
            conseil.allowed_amenagement_ids = self.env['pia.amenagement'].search([
                ('trouble', 'in', [str.lower(trouble.split(' ')[0]) for trouble in conseil.trouble_ids.mapped('name')]),
            ])

    @api.depends('name')
    def _compute_report_name(self):
        for conseil in self:
            if conseil.name == 'premier':
                conseil.report_name = '1 - '
            elif conseil.name == 'deuxieme':
                conseil.report_name = '2 - '
            elif conseil.name == 'troisieme':
                conseil.report_name = '3 - '
            else:
                conseil.report_name = '(supp) - '
            conseil.report_name += conseil.eleve_id.name

    @api.depends('intervenant_ids')
    def _compute_referals(self):
        for conseil in self:
            conseil.logo_id = False
            conseil.instit_id = False
            for inter in conseil.intervenant_ids:
                if inter.fonction == 'logo':
                    conseil.logo_id = inter
                elif inter.fonction == 'instit':
                    conseil.instit_id = inter
